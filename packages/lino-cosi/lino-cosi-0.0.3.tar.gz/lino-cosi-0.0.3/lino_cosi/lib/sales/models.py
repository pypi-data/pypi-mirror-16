# -*- coding: UTF-8 -*-
# Copyright 2008-2016 Luc Saffre
# This file is part of Lino Cosi.
#
# Lino Cosi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Cosi is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Cosi.  If not, see
# <http://www.gnu.org/licenses/>.


"""Database models for `lino_cosi.lib.sales`.

"""

from __future__ import unicode_literals

from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

from lino.api import dd, rt
from lino.core import actions
from lino.utils.xmlgen.html import E
from lino.utils.mldbc.mixins import BabelNamed
from lino.modlib.notify.utils import body_subject_to_elems

from lino_xl.lib.excerpts.mixins import Certifiable
from lino_cosi.lib.vat.utils import add_vat, remove_vat, HUNDRED
from lino_cosi.lib.vat.mixins import QtyVatItemBase, VatDocument
from lino_cosi.lib.vat.mixins import get_default_vat_regime, myround
from lino_cosi.lib.sepa.mixins import Payable
from lino_cosi.lib.ledger.mixins import Matching, SequencedVoucherItem
from lino_cosi.lib.ledger.models import Voucher
from lino_cosi.lib.ledger.choicelists import TradeTypes
from lino_cosi.lib.ledger.choicelists import VoucherTypes
from lino_cosi.lib.ledger.ui import PartnerVouchers, ByJournal


TradeTypes.sales.update(
    price_field_name='sales_price',
    price_field_label=_("Sales price"),
    base_account_field_name='sales_account',
    base_account_field_label=_("Sales Base account"),
    vat_account_field_name='sales_vat_account',
    vat_account_field_label=_("Sales VAT account"),
    partner_account_field_name='clients_account',
    partner_account_field_label=_("Clients account"))

TradeTypes.wages.update(
    partner_account_field_name='wages_account',
    partner_account_field_label=_("Wages account"))

TradeTypes.clearings.update(
    partner_account_field_name='clearings_account',
    partner_account_field_label=_("Clearings account"))

dd.inject_field(
    'contacts.Partner', 'invoice_recipient',
    dd.ForeignKey(
        'contacts.Partner',
        verbose_name=_("Invoicing address"),
        blank=True, null=True,
        help_text=_("Redirect to another partner all invoices which "
                    "should go to this partner.")))

dd.inject_field(
    'contacts.Partner', 'paper_type',
    dd.ForeignKey('sales.PaperType', null=True, blank=True))


# class Channels(dd.ChoiceList):
#     label = _("Channel")
# add = Channels.add_item
# add('P', _("Paper"), 'paper')
# add('E', _("E-mail"), 'email')


class PaperType(BabelNamed):
    """Which paper (document template) to use when printing an invoice.

    First use case is to differentiate between invoices to get printed
    either on a company letterpaper for expedition via paper mail or
    into an email-friendly pdf file.

    """

    templates_group = 'sales/VatProductInvoice'

    class Meta:
        app_label = 'sales'
        abstract = dd.is_abstract_model(__name__, 'PaperType')
        verbose_name = _("Paper type")
        verbose_name_plural = _("Paper types")

    template = models.CharField(_("Template"), max_length=200, blank=True)

    @dd.chooser(simple_values=True)
    def template_choices(cls):
        bm = rt.modules.printing.BuildMethods.get_system_default()
        return rt.find_template_config_files(
            bm.template_ext, cls.templates_group)


class PaperTypes(dd.Table):
    model = 'sales.PaperType'
    column_names = 'name template *'


# class InvoiceStates(dd.Workflow):
#     """List of the possible values for the state of an :class:`Invoice`.

#     """
#     pass

# add = InvoiceStates.add_item
# add('10', _("Draft"), 'draft', editable=True)
# add('20', _("Registered"), 'registered', editable=False)
# add('30', _("Signed"), 'signed', editable=False)
# add('40', _("Sent"), 'sent', editable=False)
# add('50', _("Paid"), 'paid', editable=False)


# @dd.receiver(dd.pre_analyze)
# def sales_workflow(sender=None, **kw):
#     InvoiceStates.registered.add_transition(
#         _("Register"), states='draft', icon_name='accept')
#     InvoiceStates.draft.add_transition(
#         _("Deregister"), states="registered", icon_name='pencil')
#     # InvoiceStates.submitted.add_transition(_("Submit"),states="registered")

class SalesDocument(VatDocument, Certifiable):
    """Common base class for `orders.Order` and :class:`VatProductInvoice`.

    Subclasses must either add themselves a `date` field (as does
    Order) or inherit it from Voucher (as does VatProductInvoice)


    """

    auto_compute_totals = True

    print_items_table = None
    """Which table (column layout) to use in the printed document.

    :class:`ItemsByInvoicePrint`
    :class:`ItemsByInvoicePrintNoQtyColumn`

    """

    class Meta:
        abstract = True

    language = dd.LanguageField()

    subject = models.CharField(_("Subject line"), max_length=200, blank=True)
    intro = models.TextField("Introductive Text", blank=True)
    
    paper_type = dd.ForeignKey('sales.PaperType', null=True, blank=True)
    # channel = Channels.field(default=Channels.paper.as_callable())

    def get_printable_type(self):
        return self.journal

    def get_print_language(self):
        return self.language or self.partner.language or \
            dd.get_default_language()

    def get_trade_type(self):
        return TradeTypes.sales

    def add_voucher_item(self, product=None, qty=None, **kw):
        Product = rt.modules.products.Product
        if product is not None:
            if not isinstance(product, Product):
                product = Product.objects.get(pk=product)
            # if qty is None:
                # qty = Duration(1)
        kw['product'] = product

        kw['qty'] = qty
        return super(SalesDocument, self).add_voucher_item(**kw)

    def get_excerpt_templates(self, bm):
        """Overrides
        :meth:`lino_xl.lib.excerpts.mixins.Certifiable.get_excerpt_templates`.

        """
        pt = self.paper_type or self.partner.paper_type
        if pt and pt.template:
            return [pt.template]


class SalesDocuments(PartnerVouchers):
    pass


class VatProductInvoice(SalesDocument, Payable, Voucher, Matching):
    """A sales invoice is a legal document which describes that something
    (the invoice items) has been sold to a given partner. The partner
    can be either a private person or an organization.

    Inherits from :class:`lino_cosi.lib.ledger.models.Voucher`.

    .. attribute:: balance_before

       The balance of previous payments or debts. On a printed
       invoice, this amount should be mentioned and added to the
       invoice's amount in order to get the total amount to pay.

    .. attribute:: balance_to_pay

       The balance of all movements matching this invoice.

    """
    class Meta:
        app_label = 'sales'
        abstract = dd.is_abstract_model(__name__, 'VatProductInvoice')
        verbose_name = _("Product invoice")
        verbose_name_plural = _("Product invoices")

    quick_search_fields = "partner__name subject"

    # order = dd.ForeignKey('orders.Order', blank=True, null=True)

    # def full_clean(self, *args, **kw):
    #     if self.due_date is None:
    #         if self.payment_term is not None:
    #             self.due_date = self.payment_term.get_due_date(
    #                 self.voucher_date)
    #     # SalesDocument.before_save(self)
    #     # ledger.LedgerDocumentMixin.before_save(self)
    #     super(VatProductInvoice, self).full_clean(*args, **kw)

    # def before_state_change(self,ar,old,new):
        # if new.name == 'registered':
            # self.compute_totals()
        # elif new.name == 'draft':
            # pass
        # super(VatProductInvoice,self).before_state_change(ar,old,new)

    @classmethod
    def get_registrable_fields(cls, site):
        for f in super(VatProductInvoice, cls).get_registrable_fields(site):
            yield f
        yield 'due_date'
        # yield 'order'

        yield 'voucher_date'
        yield 'entry_date'
        yield 'user'
        # yield 'item_vat'

    def get_print_items(self, ar):
        """
        For usage in an appy template::

            do text
            from table(obj.get_print_items(ar))

        """
        return self.print_items_table.request(self)

    @dd.virtualfield(dd.PriceField(_("Balance to pay")))
    def balance_to_pay(self, ar):
        Movement = rt.models.ledger.Movement
        qs = Movement.objects.filter(
            partner=self.get_partner(),
            cleared=False,
            match=self.match or self.get_default_match())
        return Movement.get_balance(not self.journal.dc, qs)

    @dd.virtualfield(dd.PriceField(_("Balance before")))
    def balance_before(self, ar):
        """"""
        Movement = rt.models.ledger.Movement
        qs = Movement.objects.filter(
            partner=self.get_partner(),
            cleared=False,
            value_date__lte=self.voucher_date)
        qs = qs.exclude(voucher=self)
        return Movement.get_balance(not self.journal.dc, qs)


class InvoiceDetail(dd.FormLayout):
    main = "general more ledger"

    totals = dd.Panel("""
    total_base
    total_vat
    total_incl
    workflow_buttons
    """, label=_("Totals"))

    invoice_header = dd.Panel("""
    voucher_date partner vat_regime
    #order subject your_ref match
    payment_term due_date:20 paper_type printed
    """, label=_("Header"))  # sales_remark

    general = dd.Panel("""
    invoice_header:60 totals:20
    ItemsByInvoice
    """, label=_("General"))

    more = dd.Panel("""
    id user language #project #item_vat
    intro
    """, label=_("More"))

    ledger = dd.Panel("""
    entry_date journal accounting_period number narration
    ledger.MovementsByVoucher
    """, label=_("Ledger"))


class Invoices(SalesDocuments):
    model = 'sales.VatProductInvoice'
    # order_by = ["-id"]
    order_by = ["journal", "number"]
    column_names = "id voucher_date partner total_incl user *"
    detail_layout = InvoiceDetail()
    insert_layout = dd.FormLayout("""
    partner voucher_date
    subject
    """, window_size=(40, 'auto'))
    # parameters = dict(
    #     state=VoucherStates.field(blank=True),
    #     **SalesDocuments.parameters)

    # start_at_bottom = True

    # @classmethod
    # def get_request_queryset(cls, ar):
    #     qs = super(Invoices, cls).get_request_queryset(ar)
    #     pv = ar.param_values
    #     if pv.state:
    #         qs = qs.filter(state=pv.state)
    #     return qs


class InvoicesByJournal(Invoices, ByJournal):
    """Shows all invoices of a given journal (whose `voucher_type` must be
    :class:`VatProductInvoice`)

    """
    quick_search_fields = "partner subject"
    order_by = ["-number"]
    params_panel_hidden = True
    params_layout = "partner year state cleared"
    column_names = "number_with_year voucher_date due_date " \
        "partner " \
        "total_incl subject:10 " \
        "workflow_buttons *"


class DueInvoices(Invoices):
    """Shows all due product invoices."""
    label = _("Due invoices")
    order_by = ["due_date"]

    column_names = "due_date journal__ref number " \
        "partner " \
        "total_incl balance_before balance_to_pay *"

    @classmethod
    def param_defaults(cls, ar, **kw):
        kw = super(DueInvoices, cls).param_defaults(ar, **kw)
        kw.update(cleared=dd.YesNo.no)
        return kw


class ProductDocItem(QtyVatItemBase):
    """Mixin for voucher items which potentially refer to a product.

    .. attribute:: product
    .. attribute:: description

       A multi-line rich text to be printed in the resulting printable
       document.

    .. attribute:: discount

    """
    class Meta:
        abstract = True

    product = models.ForeignKey('products.Product', blank=True, null=True)
    description = dd.RichTextField(
        _("Description"), blank=True, null=True)
    discount = dd.PercentageField(_("Discount"), blank=True, null=True)

    def get_base_account(self, tt):
        if self.product is None:
            return tt.get_base_account()
        return tt.get_product_base_account(self.product)
        # return self.voucher.journal.chart.get_account_by_ref(ref)

    def discount_changed(self, ar):
        if not self.product:
            return

        tt = self.voucher.get_trade_type()
        catalog_price = tt.get_catalog_price(self.product)

        if catalog_price is None:
            return
        # assert self.vat_class == self.product.vat_class
        rule = self.get_vat_rule()
        if rule is None:
            return
        cat_rule = rt.modules.vat.VatRule.get_vat_rule(
            get_default_vat_regime, self.get_vat_class(tt),
            dd.plugins.countries.get_my_country(),
            dd.today())
        if cat_rule is None:
            return
        if rule.rate != cat_rule.rate:
            catalog_price = remove_vat(catalog_price, cat_rule.rate)
            catalog_price = add_vat(catalog_price, cat_rule.rate)

        if self.discount is None:
            self.unit_price = myround(catalog_price)
        else:
            self.unit_price = myround(
                catalog_price * (HUNDRED - self.discount) / HUNDRED)
        self.unit_price_changed(ar)

    def product_changed(self, ar):
        if self.product:
            self.title = self.product.name
            self.description = self.product.description
            if self.qty is None:
                self.qty = Decimal("1")
            self.discount_changed(ar)


class InvoiceItem(ProductDocItem, SequencedVoucherItem):
    """An item of a sales invoice."""
    class Meta:
        app_label = 'sales'
        abstract = dd.is_abstract_model(__name__, 'InvoiceItem')
        verbose_name = _("Product invoice item")
        verbose_name_plural = _("Product invoice items")

    voucher = models.ForeignKey(
        'sales.VatProductInvoice', related_name='items')
    title = models.CharField(_("Heading"), max_length=200, blank=True)
    # ship_ref = models.CharField(
    #     _("Shipment reference"), max_length=200, blank=True)
    # ship_date = models.DateField(_("Shipment date"), blank=True, null=True)


class InvoiceItems(dd.Table):
    """Shows all sales invoice items."""
    model = 'sales.InvoiceItem'
    auto_fit_column_widths = True
    column_names = "product title discount unit_price qty total_incl *"
    # hidden_columns = "seqno description total_base total_vat"

    detail_layout = dd.DetailLayout("""
    seqno product discount
    unit_price qty total_base total_vat total_incl
    title
    description""", window_size=(80, 20))

    insert_layout = """
    product discount qty
    title
    """

    stay_in_grid = True


class ItemsByInvoice(InvoiceItems):
    label = _("Content")
    master_key = 'voucher'
    order_by = ["seqno"]



class ItemsByInvoicePrint(ItemsByInvoice):
    """The table used to render items in a printable document.

    .. attribute:: description_print

        TODO: write more about it.

    """
    column_names = "description_print unit_price qty total_incl"
    include_qty_in_description = False

    @dd.displayfield(_("Description"))
    def description_print(cls, self, ar):
        elems = body_subject_to_elems(ar, self.title, self.description)
        # dd.logger.info("20160511a %s", cls)
        if cls.include_qty_in_description:
            if self.qty != 1:
                elems += [
                    " ",
                    _("({qty}*{unit_price}/{unit})").format(
                        qty=self.quantity,
                        unit=self.product.delivery_unit,
                        unit_price=self.unit_price)]
        e = E.div(*elems)
        # dd.logger.info("20160704d %s", E.tostring(e))
        return e
                

class ItemsByInvoicePrintNoQtyColumn(ItemsByInvoicePrint):
    """Alternative column layout to be used when printing an invoice.
    """
    column_names = "description_print total_incl"
    include_qty_in_description = True
    hide_sums = True


VatProductInvoice.print_items_table = ItemsByInvoicePrint


class InvoiceItemsByProduct(InvoiceItems):
    master_key = 'product'
    column_names = "voucher voucher__partner qty title \
description:20x1 discount unit_price total_incl total_base total_vat"
    editable = False
    # auto_fit_column_widths = True


class SignAction(actions.Action):
    label = "Sign"

    def run_from_ui(self, ar):

        def ok(ar):
            for row in ar.selected_rows:
                row.instance.user = ar.get_user()
                row.instance.save()
            ar.success(refresh=True)

        ar.confirm(
            ok, _("Going to sign %d documents as user %s. Are you sure?") % (
                len(ar.selected_rows),
                ar.get_user()))


class DocumentsToSign(Invoices):
    use_as_default_table = False
    filter = dict(user__isnull=True)
    # can_add = perms.never
    column_names = "number:4 #order voucher_date " \
        "partner:10 " \
        "subject:10 total_incl total_base total_vat "
    # actions = Invoices.actions + [ SignAction() ]


class InvoicesByPartner(Invoices):
    # model = 'sales.VatProductInvoice'
    order_by = ["-voucher_date", '-id']
    master_key = 'partner'
    column_names = "voucher_date journal__ref number total_incl "\
                   "workflow_buttons *"


# class SalesByPerson(SalesDocuments):
    # column_names = "journal:4 number:4 date:8 " \
                   # "total_incl total_base total_vat *"
    # order_by = ["date"]
    # master_key = 'person'


@dd.receiver(dd.pre_analyze)
def add_voucher_type(sender, **kw):
    VoucherTypes.add_item('sales.VatProductInvoice', InvoicesByJournal)


class ProductDetailMixin(dd.DetailLayout):
    sales = dd.Panel("""
    sales.InvoiceItemsByProduct
    """, label=dd.plugins.sales.verbose_name)
    

class PartnerDetailMixin(dd.DetailLayout):
    sales = dd.Panel("""
    invoice_recipient vat_regime payment_term paper_type
    sales.InvoicesByPartner
    """, label=dd.plugins.sales.verbose_name)



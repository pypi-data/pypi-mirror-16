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

"""
Database models for `lino_cosi.lib.finan`.
"""
from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

from django.db import models

from lino_cosi.lib.accounts.utils import ZERO, DEBIT, CREDIT
from lino_cosi.lib.ledger.fields import DcAmountField
from lino_cosi.lib.ledger.choicelists import VoucherTypes
from lino_cosi.lib.ledger.roles import LedgerUser, LedgerStaff
from lino_cosi.lib.ledger.mixins import ProjectRelated
from lino_cosi.lib.sepa.mixins import BankAccount

from lino.api import dd, rt, _

from .mixins import (FinancialVoucher, FinancialVoucherItem,
                     DatedFinancialVoucher, DatedFinancialVoucherItem)



ledger = dd.resolve_app('ledger')


def warn_jnl_account(jnl):
    fld = jnl._meta.get_field('account')
    raise Warning(_("Field '{0}' in journal '{0}' is empty!").format(
        fld.verbose_name, jnl))


class ShowSuggestions(dd.Action):
    # started as a copy of ShowSlaveTable
    # TABLE2ACTION_ATTRS = tuple('help_text icon_name label sort_index'.split())
    TABLE2ACTION_ATTRS = tuple('help_text label sort_index'.split())
    show_in_bbar = False
    show_in_workflow = True
    readonly = False

    @classmethod
    def get_actor_label(self):
        return self._label or self.slave_table.label

    def attach_to_actor(self, actor, name):
        if actor.suggestions_table is None:
            # logger.info("%s has no suggestions_table", actor)
            return  # don't attach
        if isinstance(actor.suggestions_table, basestring):
            T = rt.modules.resolve(actor.suggestions_table)
            if T is None:
                raise Exception("No table named %s" % actor.suggestions_table)
            actor.suggestions_table = T
        for k in self.TABLE2ACTION_ATTRS:
            setattr(self, k, getattr(actor.suggestions_table, k))
        return super(ShowSuggestions, self).attach_to_actor(actor, name)

    # def get_action_permission(self, ar, obj, state):
        
    #     return super(ShowSuggestions, self).get_action_permission(
    #         ar, obj, state)

    def run_from_ui(self, ar, **kw):
        obj = ar.selected_rows[0]
        sar = ar.spawn(ar.actor.suggestions_table, master_instance=obj)
        js = ar.renderer.request_handler(sar)
        ar.set_response(eval_js=js)


class JournalEntry(DatedFinancialVoucher, ProjectRelated):
    """This is the model for "journal entries" ("operations diverses").

    """
    class Meta:
        app_label = 'finan'
        abstract = dd.is_abstract_model(__name__, 'JournalEntry')
        verbose_name = _("Journal Entry")
        verbose_name_plural = _("Journal Entries")

    def get_wanted_movements(self):
        # dd.logger.info("20151211 FinancialVoucher.get_wanted_movements()")
        amount, movements_and_items = self.get_finan_movements()
        if amount:
            raise Exception("Missing amount %s in movements" % amount)
        return movements_and_items


class PaymentOrder(FinancialVoucher):
    """A **payment order** is when a user instructs a bank to execute a
    series of outgoing transactions from a given bank account.

    """
    class Meta:
        app_label = 'finan'
        abstract = dd.is_abstract_model(__name__, 'PaymentOrder')
        verbose_name = _("Payment Order")
        verbose_name_plural = _("Payment Orders")

    total = dd.PriceField(_("Total"), blank=True, null=True)
    execution_date = models.DateField(
        _("Execution date"), blank=True, null=True)

    def get_wanted_movements(self):
        """Implements
        :meth:`lino_cosi.lib.ledger.models.Voucher.get_wanted_movements`
        for payment orders.

        The generated movements

        """
        # dd.logger.info("20151211 cosi.PaymentOrder.get_wanted_movements()")
        acc = self.journal.account
        if not acc:
            warn_jnl_account(self.journal)
        amount, movements_and_items = self.get_finan_movements()
        self.total = - amount
        for m, i in movements_and_items:
            yield m
            if acc.needs_partner:
                yield self.create_movement(
                    i, acc, m.project, not m.dc, m.amount,
                    partner=m.partner, match=m.match or m.get_default_match())
        if not acc.needs_partner:
            yield self.create_movement(
                None, acc, None, not self.journal.dc, amount)

    def add_item_from_due(self, obj, **kwargs):
        # if obj.bank_account is None:
        #     return
        i = super(PaymentOrder, self).add_item_from_due(obj, **kwargs)
        i.bank_account = obj.bank_account
        return i


class BankStatement(DatedFinancialVoucher):
    """A **bank statement** is a document issued by the bank, which
    reports all transactions which occured on a given account during a
    given period.

    .. attribute:: balance1

        The old (or start) balance.

    .. attribute:: balance2

        The new (or end) balance.

    """
    class Meta:
        app_label = 'finan'
        abstract = dd.is_abstract_model(__name__, 'BankStatement')
        verbose_name = _("Bank Statement")
        verbose_name_plural = _("Bank Statements")

    balance1 = dd.PriceField(_("Old balance"), default=ZERO)
    balance2 = dd.PriceField(_("New balance"), default=ZERO, blank=True)

    def get_previous_voucher(self):
        if not self.journal_id:
            #~ logger.info("20131005 no journal")
            return None
        qs = self.__class__.objects.filter(
            journal=self.journal).order_by('-voucher_date')
        if qs.count() > 0:
            #~ logger.info("20131005 no other vouchers")
            return qs[0]

    def on_create(self, ar):
        super(BankStatement, self).on_create(ar)
        if self.balance1 == ZERO:
            prev = self.get_previous_voucher()
            if prev is not None:
                #~ logger.info("20131005 prev is %s",prev)
                self.balance1 = prev.balance2

    def get_wanted_movements(self):
        # dd.logger.info("20151211 cosi.BankStatement.get_wanted_movements()")
        a = self.journal.account
        if not a:
            warn_jnl_account(self.journal)
        amount, movements_and_items = self.get_finan_movements()
        self.balance2 = self.balance1 + amount
        for m, i in movements_and_items:
            yield m
        yield self.create_movement(None, a, None, self.journal.dc, amount)


class JournalEntryItem(DatedFinancialVoucherItem):
    """An item of a :class:`JournalEntry`."""
    class Meta:
        app_label = 'finan'
        verbose_name = _("Journal Entry item")
        verbose_name_plural = _("Journal Entry items")
    voucher = dd.ForeignKey('finan.JournalEntry', related_name='items')
    debit = DcAmountField(DEBIT, _("Debit"))
    credit = DcAmountField(CREDIT, _("Credit"))


class BankStatementItem(DatedFinancialVoucherItem):
    """An item of a :class:`BankStatement`."""
    class Meta:
        app_label = 'finan'
        verbose_name = _("Bank Statement item")
        verbose_name_plural = _("Bank Statement items")
    voucher = dd.ForeignKey('finan.BankStatement', related_name='items')
    debit = DcAmountField(DEBIT, _("Income"))
    credit = DcAmountField(CREDIT, _("Expense"))


class PaymentOrderItem(BankAccount, FinancialVoucherItem):
    """An item of a :class:`PaymentOrder`."""
    class Meta:
        app_label = 'finan'
        verbose_name = _("Payment Order item")
        verbose_name_plural = _("Payment Order items")

    voucher = dd.ForeignKey('finan.PaymentOrder', related_name='items')
    # bank_account = dd.ForeignKey('sepa.Account', blank=True, null=True)

    # def partner_changed(self, ar):
    #     FinancialVoucherItem.partner_changed(self, ar)
    #     BankAccount.partner_changed(self, ar)

    # def full_clean(self, *args, **kwargs):
        
    #     super(PaymentOrderItem, self).full_clean(*args, **kwargs)

# dd.update_field(PaymentOrderItem, 'iban', blank=True)
# dd.update_field(PaymentOrderItem, 'bic', blank=True)


class JournalEntryDetail(dd.FormLayout):
    main = "general ledger"

    general = dd.Panel("""
    voucher_date user narration workflow_buttons
    finan.ItemsByJournalEntry
    """, label=_("General"))

    ledger = dd.Panel("""
    journal accounting_period number id
    ledger.MovementsByVoucher
    """, label=_("Ledger"))


class PaymentOrderDetail(JournalEntryDetail):
    general = dd.Panel("""
    voucher_date user narration total execution_date workflow_buttons
    finan.ItemsByPaymentOrder
    """, label=_("General"))


class BankStatementDetail(JournalEntryDetail):
    general = dd.Panel("""
    voucher_date balance1 balance2 user workflow_buttons
    finan.ItemsByBankStatement
    """, label=_("General"))


class FinancialVouchers(dd.Table):
    """Base class for the default tables of all other financial voucher
    types (:class:`JournalEntries` , :class:`PaymentOrders` and
    :class:`BankStatemens`).

    """
    model = 'finan.JournalEntry'
    required_roles = dd.login_required(LedgerUser)
    params_panel_hidden = True
    order_by = ["id", "voucher_date"]
    parameters = dict(
        pyear=ledger.FiscalYears.field(blank=True),
        #~ ppartner=models.ForeignKey('contacts.Partner',blank=True,null=True),
        pjournal=ledger.JournalRef(blank=True))
    params_layout = "pjournal pyear"
    detail_layout = JournalEntryDetail()
    insert_layout = dd.FormLayout("""
    voucher_date
    narration
    """, window_size=(40, 'auto'))

    suggest = ShowSuggestions()
    suggestions_table = None  # 'finan.SuggestionsByJournalEntry'

    @classmethod
    def get_request_queryset(cls, ar):
        qs = super(FinancialVouchers, cls).get_request_queryset(ar)
        if not isinstance(qs, list):
            if ar.param_values.pyear:
                qs = qs.filter(accounting_period__year=ar.param_values.pyear)
            if ar.param_values.pjournal:
                qs = qs.filter(journal=ar.param_values.pjournal)
        return qs


class JournalEntries(FinancialVouchers):
    suggestions_table = 'finan.SuggestionsByJournalEntry'
    column_names = "number_with_year voucher_date "\
                   "accounting_period workflow_buttons *"


class PaymentOrders(FinancialVouchers):
    """The table of all :class:`PaymentOrder` vouchers."""
    model = 'finan.PaymentOrder'
    column_names = "number voucher_date narration total execution_date "\
                   "accounting_period workflow_buttons *"
    detail_layout = PaymentOrderDetail()
    suggestions_table = 'finan.SuggestionsByPaymentOrder'


class BankStatements(FinancialVouchers):
    """The table of all :class:`BankStatement` vouchers."""
    model = 'finan.BankStatement'
    column_names = "number_with_year voucher_date balance1 balance2 " \
                   "accounting_period workflow_buttons *"
    detail_layout = BankStatementDetail()
    insert_layout = """
    voucher_date
    balance1
    """
    suggestions_table = 'finan.SuggestionsByBankStatement'


class AllBankStatements(BankStatements):
    required_roles = dd.login_required(LedgerStaff)


class AllJournalEntries(JournalEntries):
    required_roles = dd.login_required(LedgerStaff)


class AllPaymentOrders(PaymentOrders):
    required_roles = dd.login_required(LedgerStaff)


class PaymentOrdersByJournal(ledger.ByJournal, PaymentOrders):
    pass


class JournalEntriesByJournal(ledger.ByJournal, JournalEntries):
    pass


class BankStatementsByJournal(ledger.ByJournal, BankStatements):
    pass


class ItemsByVoucher(dd.Table):
    order_by = ["seqno"]
    column_names = "date partner account match remark debit credit seqno *"
    master_key = 'voucher'
    auto_fit_column_widths = True
    # hidden_columns = 'id amount dc seqno'
    suggest = ShowSuggestions()
    suggestions_table = None  # 'finan.SuggestionsByJournalEntry'


class ItemsByJournalEntry(ItemsByVoucher):
    model = 'finan.JournalEntryItem'
    column_names = "date partner account match remark debit credit seqno *"


class ItemsByBankStatement(ItemsByVoucher):
    model = 'finan.BankStatementItem'
    column_names = "date partner account match remark debit credit "\
                   "workflow_buttons seqno *"
    suggestions_table = 'finan.SuggestionsByBankStatementItem'


class ItemsByPaymentOrder(ItemsByVoucher):
    label = _("Content")
    model = 'finan.PaymentOrderItem'
    column_names = "seqno partner workflow_buttons bank_account match "\
                   "amount remark *"
    suggestions_table = 'finan.SuggestionsByPaymentOrderItem'


# class ItemsByGrouper(ItemsByVoucher):
#     model = 'finan.GrouperItem'
#     column_names = "seqno partner match amount remark *"


class FillSuggestionsToVoucher(dd.Action):
    """Fill selected suggestions from a SuggestionsByVoucher table into a
    financial voucher.

    This creates one voucher item for each selected row.

    """
    label = _("Fill")
    icon_name = 'lightning'
    http_method = 'POST'
    select_rows = False

    def run_from_ui(self, ar, **kw):
        voucher = ar.master_instance
        seqno = None
        n = 0
        for obj in ar.selected_rows:
            i = voucher.add_item_from_due(obj, seqno=seqno)
            if i is not None:
                # dd.logger.info("20151117 gonna full_clean %s", obj2str(i))
                i.full_clean()
                # dd.logger.info("20151117 gonna save %s", obj2str(i))
                i.save()
                # dd.logger.info("20151117 ok")
                seqno = i.seqno + 1
                n += 1

        msg = _("%d items have been added to %s.") % (n, voucher)
        logger.info(msg)
        kw.update(close_window=True)
        ar.success(msg, **kw)


class FillSuggestionsToVoucherItem(FillSuggestionsToVoucher):
    """Fill the selected suggestions as items to the voucher. The *first*
    selected suggestion does not create a new item but replaces the
    item for which it was called.

    """
    def run_from_ui(self, ar, **kw):
        # compare add_item_from_due
        i = ar.master_instance
        voucher = i.voucher
        obj = ar.selected_rows[0]
        # i is the voucher item from which the suggestion table had
        # been called. obj is the first selected DueMovement object
        # print 20151217, ar.selected_rows, obj
        i.account = obj.account
        i.dc = not obj.dc
        # if voucher.journal.invert_due_dc:
        #     i.dc = not obj.dc
        # else:
        #     i.dc = obj.dc
        i.amount = obj.balance
        i.partner = obj.partner
        i.match = obj.match
        if i.amount < 0:
            i.amount = - i.amount
            i.dc = not i.dc
        i.full_clean()
        i.save()

        seqno = i.seqno
        n = 0
        for obj in ar.selected_rows[1:]:
            i = voucher.add_item_from_due(obj, seqno=seqno)
            if i is not None:
                # dd.logger.info("20151117 gonna full_clean %s", obj2str(i))
                i.on_create(ar)
                i.full_clean()
                # dd.logger.info("20151117 gonna save %s", obj2str(i))
                i.save()
                # dd.logger.info("20151117 ok")
                seqno = i.seqno + 1
                n += 1

        msg = _("%d items have been added to %s.") % (n, voucher)
        logger.info(msg)
        kw.update(close_window=True)
        ar.success(msg, **kw)


class SuggestionsByVoucher(ledger.ExpectedMovements):
    """Shows the suggested items for a given voucher, with a button to
    fill them into the current voucher.

    This is the base class for
    :class:`SuggestionsByJournalEntry`
    :class:`SuggestionsByBankStatement` and
    :class:`SuggestionsByPaymentOrder` who define the class of the
    master_instance (:attr:`master <lino.core.actors.Actor.master>`)

    This is an abstract virtual slave table.

    Every row is a :class:`DueMovement
    <lino_cosi.lib.ledger.utils.DueMovement>` object.

    """

    label = _("Suggestions")
    # column_names = 'partner project match account due_date debts payments balance *'
    column_names = 'info match due_date debts payments balance *'
    window_size = ('90%', 20)  # (width, height)

    editable = False
    auto_fit_column_widths = True
    cell_edit = False

    do_fill = FillSuggestionsToVoucher()

    @classmethod
    def get_dc(cls, ar=None):
        if ar is None:
            return None
        voucher = ar.master_instance
        if voucher is None:
            return None
        return not voucher.journal.dc

    @classmethod
    def param_defaults(cls, ar, **kw):
        kw = super(SuggestionsByVoucher, cls).param_defaults(ar, **kw)
        voucher = ar.master_instance
        kw.update(for_journal=voucher.journal)
        if not dd.plugins.finan.suggest_future_vouchers:
            kw.update(date_until=voucher.voucher_date)
        # kw.update(trade_type=vat.TradeTypes.purchases)
        return kw

    @classmethod
    def get_data_rows(cls, ar, **flt):
        #~ partner = ar.master_instance
        #~ if partner is None: return []
        flt.update(cleared=False)
        # flt.update(account__clearable=True)
        return super(SuggestionsByVoucher, cls).get_data_rows(ar, **flt)


class SuggestionsByJournalEntry(SuggestionsByVoucher):
    "A :class:`SuggestionsByVoucher` table for a :class:`JournalEntry`."
    master = 'finan.JournalEntry'


class SuggestionsByPaymentOrder(SuggestionsByVoucher):
    "A :class:`SuggestionsByVoucher` table for a :class:`PaymentOrder`."

    master = 'finan.PaymentOrder'
    # column_names = 'partner match account due_date debts payments balance bank_account *'
    column_names = 'info match due_date debts payments balance *'

    @classmethod
    def param_defaults(cls, ar, **kw):
        kw = super(SuggestionsByPaymentOrder, cls).param_defaults(ar, **kw)
        voucher = ar.master_instance
        # kw.update(journal=voucher.journal)
        kw.update(date_until=voucher.execution_date or voucher.voucher_date)
        if voucher.journal.trade_type is not None:
            kw.update(trade_type=voucher.journal.trade_type)
        # kw.update(trade_type=vat.TradeTypes.purchases)
        return kw


class SuggestionsByBankStatement(SuggestionsByVoucher):
    "A :class:`SuggestionsByVoucher` table for a :class:`BankStatement`."
    master = 'finan.BankStatement'


class SuggestionsByVoucherItem(SuggestionsByVoucher):
    """Displays the payment suggestions for a voucher item, with a button
    to fill them into the current item (creating additional items if
    more than one suggestion was selected).

    """

    do_fill = FillSuggestionsToVoucherItem()

    @classmethod
    def get_dc(cls, ar=None):
        if ar is None:
            return None
        item = ar.master_instance
        if item is None:
            return None
        return not item.voucher.journal.dc

    @classmethod
    def param_defaults(cls, ar, **kw):
        # Note that we skip immeditate parent
        kw = super(SuggestionsByVoucher, cls).param_defaults(ar, **kw)
        item = ar.master_instance
        voucher = item.voucher
        kw.update(for_journal=voucher.journal)
        if not dd.plugins.finan.suggest_future_vouchers:
            kw.update(date_until=voucher.voucher_date)
        kw.update(partner=item.partner)
        return kw


class SuggestionsByBankStatementItem(SuggestionsByVoucherItem):
    """A :class:`SuggestionsByVoucherItem` table for a
    :class:`BankStatementItem`.

    """
    master = 'finan.BankStatementItem'


class SuggestionsByPaymentOrderItem(SuggestionsByVoucherItem):
    """A :class:`SuggestionsByVoucherItem` table for a
    :class:`PaymentOrderItem`.

    """
    master = 'finan.PaymentOrderItem'


# Declare the voucher types:

VoucherTypes.add_item(JournalEntry, JournalEntriesByJournal)
VoucherTypes.add_item(PaymentOrder, PaymentOrdersByJournal)
VoucherTypes.add_item(BankStatement, BankStatementsByJournal)
# VoucherTypes.add_item(Grouper, GroupersByJournal)

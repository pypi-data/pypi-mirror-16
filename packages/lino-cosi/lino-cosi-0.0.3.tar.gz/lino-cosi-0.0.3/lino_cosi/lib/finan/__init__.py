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
Adds functionality for managing financial stuff.
See :doc:`/specs/finan`.

.. autosummary::
   :toctree:

    models
    choicelists
    mixins
    fixtures.payments

"""

from lino.api import ad, _


class Plugin(ad.Plugin):
    "See :class:`lino.core.plugin.Plugin`."

    verbose_name = _("Financial")

    needs_plugins = ['lino_cosi.lib.ledger']

    suggest_future_vouchers = False
    """Whether to suggest vouchers whose due_date is in the future.

    The default value is currently `False` because some demo fixtures
    rely on this.  But in most cases this should probably be set to
    `True` because of course a customer can pay an invoice in advance.

    You can specify this for your application::

        def setup_plugins(self):
            self.plugins.finan.suggest_future_vouchers = True
            super(Site, self).setup_plugins()

    Or, as a local system administrator you can also simply set it
    after your :data:`SITE` instantiation::

        SITE = Site(globals())
        ...
        SITE.plugins.finan.suggest_future_vouchers = True

    """

    # def setup_main_menu(self, site, profile, m):
    #     m = m.add_menu(self.app_label, self.verbose_name)
    #     ledger = site.modules.ledger
    #     for jnl in ledger.Journal.objects.filter(trade_type=''):
    #         m.add_action(jnl.voucher_type.table_class,
    #                      label=unicode(jnl),
    #                      params=dict(master_instance=jnl))

    def setup_explorer_menu(self, site, profile, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('finan.AllBankStatements')
        m.add_action('finan.AllJournalEntries')
        m.add_action('finan.AllPaymentOrders')
        # m.add_action('finan.Groupers')

# -*- coding: UTF-8 -*-
# Copyright 2015 Luc Saffre
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



from lino.core.roles import UserRole
from lino.api import _
from lino.modlib.office.roles import OfficeUser, SiteAdmin
from lino.modlib.users.choicelists import UserProfiles


class AccountingReader(UserRole):
    pass


class LedgerUser(AccountingReader):
    pass


class LedgerStaff(LedgerUser):
    pass


class SiteUser(OfficeUser, AccountingReader):
    """A normal authentified user."""
    pass


class SiteAdmin(SiteAdmin, LedgerStaff):
    """A user with all permissions."""
    pass


UserProfiles.clear()
add = UserProfiles.add_item
add('000', _("Anonymous"), UserRole, name='anonymous', readonly=True)
add('100', _("User"), SiteUser, name='user')
add('900', _("Administrator"), SiteAdmin, name='admin')

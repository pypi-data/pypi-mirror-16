# -*- coding: utf-8 -*-
# Copyright 2013-2016 Luc Saffre
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
This module contains "quick" tests that are run on a demo database
without any fixture. You can run only these tests by issuing::

  $ cd lino_cosi/projects/std
  $ python manage.py test

"""

from __future__ import unicode_literals
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

from atelier.utils import AttrDict
import json

from lino.api.shell import *

from lino.utils.djangotest import RemoteAuthTestCase


class QuickTest(RemoteAuthTestCase):

    def test01(self):
        """
        Initialization.
        """
        #~ print "20130321 test00 started"
        self.user_root = settings.SITE.user_model(
            username='root', language='en', profile='900')
        self.user_root.save()

        self.assertEqual(1 + 1, 2)
        o1 = contacts.Company(name="Example")
        o1.save()
        o2 = contacts.Company(name="Example")
        o2.save()

        p1 = contacts.Person(first_name="John", last_name="Doe")
        p1.full_clean()
        p1.save()
        p2 = contacts.Person(first_name="Johny", last_name="Doe")
        p2.full_clean()
        p2.save()

        contacts.Role(person=p1, company=o1).save()
        contacts.Role(person=p2, company=o2).save()

        evt = cal.Event()
        evt.full_clean()
        evt.save()
        guest = cal.Guest(event=evt, partner=p1)
        guest.full_clean()
        guest.save()

        # s = contacts.ContactsByOrganisation.request(o1).to_rst()
        s = contacts.RolesByCompany.request(o1).to_rst()
        # print('\n'+s)
        self.assertEqual(s, """\
========== ==============
 Person     Contact Role
---------- --------------
 John Doe
========== ==============

""")

        s = contacts.RolesByCompany.request(o2).to_rst()
        # print('\n'+s)
        self.assertEqual(s, """\
=========== ==============
 Person      Contact Role
----------- --------------
 Johny Doe
=========== ==============

""")
        utpl = "/api/contacts/Persons/{0}?fv={1}&fv=false&fv=fff&an=merge_row"
        url = utpl.format(p1.pk, p1.pk)
        res = self.client.get(url, REMOTE_USER='root')
        self.assertEqual(res.status_code, 200)
        res = AttrDict(json.loads(res.content))
        self.assertEqual(res.message, "Cannot merge an instance to itself.")
        self.assertEqual(res.success, False)

        url = utpl.format(p1.pk, '')
        res = self.client.get(url, REMOTE_USER='root')
        self.assertEqual(res.status_code, 200)
        res = AttrDict(json.loads(res.content))
        self.assertEqual(res.message, "You must specify a merge target.")
        self.assertEqual(res.success, False)

        url = utpl.format(p1.pk, p2.pk)
        res = self.client.get(url, REMOTE_USER='root')
        self.assertEqual(res.status_code, 200)
        res = AttrDict(json.loads(res.content))
        # print(res)
        expected = '<div class="htmlText"><p>Are you sure you want to merge John Doe into Johny Doe?</p><ul><li>1 Contact Persons, 1 Presences <b>will get reassigned.</b></li><li>John Doe will be deleted</li></ul></div>'
        self.assertEqual(res.message, expected)
        self.assertEqual(res.success, True)
        self.assertEqual(res.close_window, True)
        self.assertEqual(res.xcallback['buttons'], {'yes': 'Yes', 'no': 'No'})
        self.assertEqual(res.xcallback['title'], "Confirmation")
        
        url = "/callbacks/{}/yes".format(res.xcallback['id'])
        res = self.client.get(url, REMOTE_USER='root')
        self.assertEqual(res.status_code, 200)
        res = AttrDict(json.loads(res.content))
        # print(res)
        self.assertEqual(
            res.message,
            'Merged John Doe into Johny Doe. Updated 2 related rows.')
        self.assertEqual(res.success, True)

        s = contacts.Roles.request().to_rst()
        # print('\n'+s)
        self.assertEqual(s, """\
==== ============== =========== ==============
 ID   Contact Role   Person      Organization
---- -------------- ----------- --------------
 1                   Johny Doe   Example
 2                   Johny Doe   Example
==== ============== =========== ==============

""")

        s = cal.Guests.request().to_rst()
        # print('\n'+s)
        self.assertEqual(s, """\
=========== ====== ============= ======== =======================
 Partner     Role   Workflow      Remark   Event
----------- ------ ------------- -------- -----------------------
 Doe Johny          **Invited**            Event #1 (12.05.2015)
=========== ====== ============= ======== =======================

""")


        # self.fail("TODO: execute a merge action using the web interface")

        # 20130418 server traceback caused when a pdf view of a table
        # was requested through the web interface.  TypeError:
        # get_handle() takes exactly 1 argument (2 given)
        url = settings.SITE.buildurl(
            'api/countries/Countries?cw=189&cw=45&cw=45&cw=36&ch=&ch=&ch=&ch=&ch=&ch=&ci=name&ci=isocode&ci=short_code&ci=iso3&name=0&an=as_pdf')
        msg = 'Using remote authentication, but no user credentials found.'
        try:
            response = self.client.get(url)
            self.fail("Expected '%s'" % msg)
        except Exception as e:
            self.assertEqual(str(e), msg)

        response = self.client.get(url, REMOTE_USER='foo')
        self.assertEqual(response.status_code, 403,
                         "Status code for anonymous on GET %s" % url)
        from appy.pod import PodError

        """
        If oood is running, we get a 302, otherwise a PodError
        """
        try:
            response = self.client.get(url, REMOTE_USER='root')
            #~ self.assertEqual(response.status_code,200)
            result = self.check_json_result(response, 'success open_url')
            self.assertEqual(
                result['open_url'], "/media/cache/appypdf/127.0.0.1/countries.Countries.pdf")

        except PodError as e:
            pass
            #~ self.assertEqual(str(e), PodError: Extension of result file is "pdf".

    def test02(self):
        obj = ledger.AccountingPeriod()
        obj.full_clean()
        self.assertEqual(
            str(obj),
            'AccountingPeriod(start_date=2015-05-01,'
            'state=<PeriodStates.open:10>,year=<FiscalYears:15>)')


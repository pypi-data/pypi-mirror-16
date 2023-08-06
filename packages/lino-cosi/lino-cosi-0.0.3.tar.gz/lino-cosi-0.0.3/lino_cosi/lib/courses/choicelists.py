# -*- coding: UTF-8 -*-
# Copyright 2012-2016 Luc Saffre
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


from __future__ import unicode_literals
from __future__ import print_function

"""
Choicelists for :mod:`lino_cosi.lib.courses`.

"""

import logging
logger = logging.getLogger(__name__)

from django.db import models
from django.utils.translation import ugettext_lazy as _

from lino.api import dd


class CourseStates(dd.Workflow):
    required_roles = dd.required(dd.SiteAdmin)
    invoiceable = models.BooleanField(_("invoiceable"), default=True)

add = CourseStates.add_item
add('10', _("Draft"), 'draft', editable=True, invoiceable=False)
# add('20', _("Registered"), 'registered', editable=False, invoiceable=True)
add('20', _("Active"), 'active', editable=False, invoiceable=True)
add('30', _("Inactive"), 'inactive', editable=False, invoiceable=False)
add('40', _("Closed"), 'closed', editable=False, invoiceable=False)

# #~ ACTIVE_COURSE_STATES = set((CourseStates.published,CourseStates.started))
# ACTIVE_COURSE_STATES = set((CourseStates.registered, CourseStates.started))


class EnrolmentStates(dd.Workflow):
    """The list of possible states of an enrolment.

    The default implementation has the following values:
    
    .. attribute:: requested
    .. attribute:: confirmed
    .. attribute:: cancelled

    """
    verbose_name_plural = _("Enrolment states")
    required_roles = dd.required(dd.SiteAdmin)
    invoiceable = models.BooleanField(_("invoiceable"), default=True)
    uses_a_place = models.BooleanField(_("Uses a place"), default=True)

add = EnrolmentStates.add_item
add('10', _("Requested"), 'requested', invoiceable=False, uses_a_place=False)
add('20', _("Confirmed"), 'confirmed', invoiceable=True, uses_a_place=True)
add('30', _("Cancelled"), 'cancelled', invoiceable=False, uses_a_place=False)
# add('40', _("Certified"), 'certified', invoiceable=True, uses_a_place=True)
#~ add('40', _("Started"),'started')
#~ add('50', _("Success"),'success')
#~ add('60', _("Award"),'award')
#~ add('90', _("Abandoned"),'abandoned')


class CourseArea(dd.Choice):
    def __init__(
            self, value, text, name, courses_table='courses.Courses'):
        self.courses_table = courses_table
        super(CourseArea, self).__init__(value, text, name)


class CourseAreas(dd.ChoiceList):
    preferred_width = 10
    # verbose_name = _("Course area")
    # verbose_name_plural = _("Course areas")
    verbose_name = _("Layout")
    verbose_name_plural = _("Course layouts")
    item_class = CourseArea

add = CourseAreas.add_item
add('C', _("Courses"), 'default')
# add('J', _("Journeys"), 'journeys')



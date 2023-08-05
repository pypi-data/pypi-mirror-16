# -*- coding: UTF-8 -*-
# Copyright 2012-2015 Luc Saffre
#
# This file is part of Lino XL.
#
# Lino XL is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino XL is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino XL.  If not, see
# <http://www.gnu.org/licenses/>.
"""Database models for `lino_xl.lib.households`.

"""

from lino.api import dd, _
from lino.modlib.contacts.roles import ContactsStaff


class MemberRoles(dd.ChoiceList):
    """The list of allowed choices for the (:attr:`role
    <lino_xl.lib.households.models.Member.role>` of a household member.

    """
    required_roles = dd.required(ContactsStaff)
    verbose_name = _("Role")
    verbose_name_plural = _("Household member roles")

add = MemberRoles.add_item
add('01', _("Head of household"), 'head')
add('02', _("Spouse"), 'spouse')  # married
add('03', _("Partner"), 'partner')  # not married
add('04', _("Cohabitant"), 'cohabitant')  # not a relative but living here
add('05', _("Child"), 'child')  # i.e. of at least one parent
add('06', _("Relative"), 'relative')  # relative who does not live here
add('07', _("Adopted child"), 'adopted')
add('10', _("Other"), 'other')  # neither cohabitant nor relaive
# add('10', _("Child of head"), 'child_of_head')
# add('11', _("Child of partner"), 'child_of_partner')

parent_roles = (MemberRoles.head, MemberRoles.spouse,
                MemberRoles.partner, MemberRoles.cohabitant)

child_roles = (MemberRoles.child, MemberRoles.adopted)
               # MemberRoles.child_of_head, MemberRoles.child_of_partner)

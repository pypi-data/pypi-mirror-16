# -*- coding: UTF-8 -*-
# Copyright 2014 Luc Saffre
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

from django.utils.translation import ugettext_lazy as _

from lino.api import dd, rt


def objects():
    ListType = rt.modules.lists.ListType
    List = rt.modules.lists.List

    mailing = ListType(**dd.str2kw('name', _("Mailing list")))
    yield mailing

    discuss = ListType(**dd.str2kw('name', _("Discussion group")))
    yield discuss

    flags = ListType(**dd.str2kw('name', _("Flags")))
    yield flags

    yield List(list_type=mailing, **dd.str2kw('name', _("Announcements")))
    yield List(list_type=mailing, **dd.str2kw('name', _("Weekly newsletter")))

    yield List(list_type=discuss, **dd.str2kw('name', _("General discussion")))
    yield List(list_type=discuss, **dd.str2kw('name', _("Beginners forum")))
    yield List(list_type=discuss, **dd.str2kw('name', _("Developers forum")))

    yield List(list_type=flags,
               **dd.str2kw('name', _("PyCon 2014")))
    yield List(list_type=flags,
               **dd.str2kw('name', _("Free Software Day 2014")))
    yield List(list_type=flags, **dd.str2kw('name', _("Schools")))



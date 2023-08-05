# -*- coding: UTF-8 -*-
# Copyright 2009-2016 Luc Saffre
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

"""Database models for `lino_xl.lib.blogs`.

"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


from lino.api import dd
from lino import mixins
from lino.modlib.gfks.mixins import Controllable
from lino.modlib.users.mixins import ByUser, UserAuthored
from lino.modlib.printing.mixins import PrintableType, TypedPrintable


@dd.python_2_unicode_compatible
class EntryType(mixins.BabelNamed, PrintableType):

    templates_group = 'blogs/Entry'

    class Meta:
        verbose_name = _("Blog Entry Type")
        verbose_name_plural = _("Blog Entry Types")

    #~ name = models.CharField(max_length=200)
    important = models.BooleanField(
        verbose_name=_("important"),
        default=False)
    remark = models.TextField(verbose_name=_("Remark"), blank=True)

    def __str__(self):
        return self.name


# def html_text(s):
#     return '<div class="htmlText">' + s + '</div>'


class EntryTypes(dd.Table):
    model = EntryType
    column_names = 'name build_method template *'
    order_by = ["name"]

    detail_layout = """
    id name
    build_method template
    remark:60x5
    blogs.EntriesByType
    """


@dd.python_2_unicode_compatible
class Entry(TypedPrintable,
            mixins.CreatedModified,
            UserAuthored,
            Controllable):

    """
    Deserves more documentation.
    """
    class Meta:
        verbose_name = _("Blog Entry")
        verbose_name_plural = _("Blog Entries")

    language = dd.LanguageField()
    type = models.ForeignKey(EntryType, blank=True, null=True)
    # ,null=True)
    title = models.CharField(_("Heading"), max_length=200, blank=True)
    body = dd.RichTextField(_("Body"), blank=True, format='html')

    def __str__(self):
        return u'%s #%s' % (self._meta.verbose_name, self.pk)


class EntryDetail(dd.FormLayout):
    main = """
    title type:12 user:10 id
    # summary
    language:10 created modified owner build_time
    body
    """


class Entries(dd.Table):
    model = Entry
    detail_layout = EntryDetail()
    column_names = "id modified user type title * body"
    #~ hide_columns = "body"
    #~ hidden_columns = frozenset(['body'])
    order_by = ["id"]
    #~ label = _("Notes")


class MyEntries(ByUser, Entries):
    #~ master_key = 'user'
    column_names = "modified type title body *"
    #~ column_names = "date event_type type subject body *"
    #~ column_names = "date type event_type subject body_html *"
    #~ can_view = perms.is_authenticated
    order_by = ["-modified"]

    #~ def setup_request(self,req):
        #~ if req.master_instance is None:
            #~ req.master_instance = req.get_user()

#~ class NotesByProject(Notes):
    #~ master_key = 'project'
    #~ column_names = "date subject user *"
    #~ order_by = "date"

#~ class NotesByController(Notes):
    #~ master_key = 'owner'
    #~ column_names = "date subject user *"
    #~ order_by = "date"


class EntriesByType(Entries):
    master_key = 'type'
    column_names = "modified title user *"
    order_by = ["modified-"]
    #~ label = _("Notes by person")


class EntriesByController(Entries):
    master_key = 'owner'
    column_names = "modified title user *"
    order_by = ["modified-"]
    #~ label = _("Notes by person")



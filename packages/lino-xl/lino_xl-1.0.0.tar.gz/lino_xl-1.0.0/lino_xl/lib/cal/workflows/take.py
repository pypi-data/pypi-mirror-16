# -*- coding: UTF-8 -*-
# Copyright 2011-2015 Luc Saffre
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

"""Importing this from within one of your :xfile:`models.py` modules
will add the :class:`TakeEvent` action to your application's
`cal.Event`.

"""

from __future__ import unicode_literals

from lino.api import dd, _


class TakeEvent(dd.Action):
    """
    This action means that you declare to become the fully responsible
    user for this event.  Accordingly, this action is available only
    when you are not already fully responsible. You are fully
    responsible when (1) :attr:`Event.user` is set to *you*
    **and** (2) :attr:`Event.assigned_to` is *not empty*.

    Basically anybody can take any event, even if it is not assigned
    to them.


    """
    label = _("Take")
    show_in_workflow = True

    #~ icon_file = 'cancel.png'
    icon_name = 'flag_green'
    help_text = _("Take responsibility for this event.")

    def get_action_permission(self, ar, obj, state):
        if obj.user == ar.get_user():
            if obj.assigned_to is None:
                return False
        # elif obj.assigned_to != ar.get_user():
        #     return False
        return super(TakeEvent,
                     self).get_action_permission(ar, obj, state)

    def run_from_ui(self, ar, **kw):
        obj = ar.selected_rows[0]

        def ok(ar):
            obj.user = ar.get_user()
            obj.assigned_to = None
            #~ kw = super(TakeEvent,self).run(obj,ar,**kw)
            obj.save()
            ar.set_response(refresh=True)

        ar.confirm(ok, self.help_text, _("Are you sure?"))


@dd.receiver(dd.pre_analyze)
def take_workflows(sender=None, **kw):

    site = sender

    site.modules.cal.Event.take = TakeEvent()

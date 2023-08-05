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
"""Defines actions for reading electronic ID smartcards.

Installing this package makes sense only if there is exactly one
subclass of the :class:`BeIdCardHolder` model mixin among your
application's models.

When this plugin is installed, you can still easily disable it by
setting :attr:`use_java <lino.core.site.Site.use_java>` to `False` in
your :xfile:`settings.py`.

When this plugin is activated, then you must also add the `.jar` files
required by :ref:`eidreader` into your media directory, in a
subdirectory named "eidreader".  TODO: move :ref:`eidreader` to a
`static` directory in the Lino repository.

An (untested) alternative implementation of the same functionality is
:mod:`lino.modlib.eid_jslib.beid` which overrides this plugin and does
the same except that it uses `eidjslib` instead of :ref:`eidreader`.

.. autosummary::
   :toctree:

    choicelists
    mixins
    models

"""

from lino.api import ad, _


class Plugin(ad.Plugin):  # was: use_eidreader
    "See :class:`lino.core.Plugin`."

    site_js_snippets = ['beid/eidreader.js']
    media_name = 'eidreader'

    data_collector_dir = None
    """
    When this is a non-empty string containing a directory name on the
    server, then Lino writes the raw data of every eid card into a
    text file in this directory.
    """

    read_only_simulate = False

    def get_body_lines(self, site, request):
        if not site.use_java:
            return
        # p = self.build_media_url('EIDReader.jar')
        # p = self.build_media_url('eidreader.jnlp')
        p = self.build_lib_url()
        p = request.build_absolute_uri(p)
        yield '<applet name="EIDReader" code="src.eidreader.EIDReader.class"'
        # yield '        archive="%s"' % p
        yield '        codebase="%s">' % p
        # seems that you may not use another size than
        # yield '        width="0" height="0">'
        # ~ yield '<param name="separate_jvm" value="true">' # 20130913
        yield '<param name="permissions" value="all-permissions">'
        # yield '<param name="jnlp_href" value="%s">' % p
        yield '<param name="jnlp_href" value="eidreader.jnlp">'
        yield '</applet>'


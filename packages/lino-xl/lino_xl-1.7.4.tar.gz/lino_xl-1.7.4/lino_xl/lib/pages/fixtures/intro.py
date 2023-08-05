# -*- coding: UTF-8 -*-
# Copyright 2012-2016 Luc Saffre
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

"""
This fixture defines pages `/`, `/admin` and `/about`,
with automatically generated introductory content.

Currently in English, German and French.

This is no longer a "reloadable" fixture. If you say::

  python manage.py loaddata intro
  
it will overwrite existing web pages.

"""

from __future__ import unicode_literals

from lino_xl.lib.pages.builder import page, objects

page('index', 'en', '', """
Welcome to the **{{site.title}}** site.
{% if site.verbose_name %}
This is an online demo of `{{site.verbose_name}} <{{site.url}}>`__
version {{site.version}}.
{% endif %}

{% if site.admin_prefix %}

You are currently seeing the **web content** section,
whose content and layout are configurable using
the normal Django techniques.

To see what Lino really adds to a Django site,
you should go to the `Admin <{{site.admin_prefix}}/>`__ section.

{% endif %}
""")


page('index', 'fr', '', """
Bienvenue sur **{{site.title}}**.
{% if site.verbose_name %}
Ce site est une démonstration en ligne de
`{{site.verbose_name}} <{{site.url}}>`__
version {{site.version}}.
{% endif %}

{% if site.admin_prefix %}

Ceci est la section publique dont le layout et le contenu sont configurables
selon les techniques habituelles de Django.

Pour voir ce que Lino ajoute à Django, vous devriez maintenant aller 
dans la `section administrative <{{site.admin_prefix}}/>`__.


{% endif %}
""")

page('index', 'de', '', """
Willkommen auf {{site.title}}.
{% if site.verbose_name %}
Diese Site ist eine Online-Demo von
`{{site.verbose_name}} <{{site.url}}>`__
version {{site.version}}.
{% endif %}

{% if site.admin_prefix %}

Dies ist der öffentliche Bereich, dessen Layout
und Inhalt frei konfigurierbar sind wie bei jeder Django-Site.

Um das Besondere an Lino zu sehen, sollten Sie nun
in den `Verwaltungsbereich <{{site.admin_prefix}}/>`__ gehen.

{% endif %}
""")

page('index', 'et', '', """
Tere tulemast saidil {{site.title}}.
{% if site.verbose_name %}
Siin jookseb
`{{site.verbose_name}} <{{site.url}}>`__
versioon {{site.version}}.
{% endif %}

{% if site.admin_prefix %}

Praegu oled kasutajaliideses "Pages", mille kujundus ja sisu saab
seadistada nii nagu Django saitidel ikka.

Um das Besondere an Lino zu sehen, sollten Sie nun
in den `Verwaltungsbereich <{{site.admin_prefix}}/>`__ gehen.

{% endif %}
""")


page('about', 'en', 'About', """
This website is a life demonstration of
`{{site.verbose_name}} <{{site.url}}>`__.    
""")

page('about', 'fr', 'À propos', """
Ce site est une démonstration en ligne de
`{{site.verbose_name}} <{{site.url}}>`__.
""")

page('about', 'de', 'Info', """
Dies ist eine online-Demo von `{{site.verbose_name}} <{{site.url}}>`__.
""")


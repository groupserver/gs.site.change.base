====================
``site.change.base``
====================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The core site administration system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-03-12
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

Introduction
============

The ``gs.site.change.base`` egg provides the core code for the
pages that change a site. It provides to main interfaces:

#.  The `Site Administration area`_ on the site homepage, and
#.  The *Change Site* page, which contains exactly the same
    things as the Change Site page. For historical reasons the
    Change Site page is located at ``/admindivision``.

Site Administration Area
========================

The site administration area provides many viewlet managers to
display links and notifications to the site administrator. Both
the Change Site page and the Site Administration viewlet the
structure, which is is as follows::

  ┌─ #gs-site-change-base-adminstuff ────────────────────────────┐
  │                                                              │
  │    Interface: gs.site.change.base.interfaces.ISiteAdminStuff │
  │    (Big and complex administrator tasks.)                    │
  │                                                              │
  │┌─ #gs-site-change-base-adminstuff-adminlinks ───────────────┐│
  ││                                                            ││
  ││    (A viewlet to provide the simple links.)                ││
  ││                                                            ││
  ││┌─ #gs-site-change-base-adminstuff-adminlinks-manager ─────┐││
  │││                                                          │││
  │││ Interface: gs.site.change.base.interfaces.ISiteAdminLinks│││
  │││ (A bunch of simple links to administration pages.)       │││
  │││                                                          │││
  ││└──────────────────────────────────────────────────────────┘││
  │└────────────────────────────────────────────────────────────┘│
  └──────────────────────────────────────────────────────────────┘

Examples
--------

A simple link to an administration page would have a ZCML
declaration similar to the following:

.. code-highlight: xml

  <browser:viewlet
    name="gs-some-admin-product-link"
    manager="gs.site.change.base.interfaces.ISiteAdminLinks"
    templates="browser/templates/adminlink.pt"
    permission="zope2.ManageProperties"
    weight="20"/>

The page-template itself would be very simple:

.. code-highlight: xml

  <li id="gs-some-admin-product-link">
    <a href="/gs-some-admin-product.html">A link to a admin page</a></li>

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.site.change.base/
- Translations:
  https://www.transifex.com/projects/p/gs-site-change-base/
- Questions and comments to
  http://groupserver.org/groups/development/
- Report bugs at https://redmine.iopen.net/projects/groupserver/

.. _GroupServer.org: http://groupserver.org/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/
.. _onlinegroups.net: https://onlinegroups.net/
.. _GroupServer: http://groupserver.org/

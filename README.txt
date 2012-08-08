Introduction
============

The ``gs.site.change.base`` egg provides the core code for the pages that
change a site. It provides to main interfaces:

#.  The `Site Administration area`_ on the site homepage, and
#.  The *Change Site* page, which contains exactly the same things as the
    Change Site page. For historical reasons the Change Site page is
    located at ``/admindivision``.

Site Administration Area
========================

The site administration area provides many viewlet managers to display
links and notifications to the site administrator. Both the Change Site
page and the Site Administration viewlet the structure, which is is as
follows::

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

A simple link to an administration page would have a ZCML declaration
similar to the following::

  <browser:viewlet
    name="gs-some-admin-product-link"
    manager="gs.site.change.base.interfaces.ISiteAdminLinks"
    templates="browser/templates/adminlink.pt"
    permission="zope2.ManageProperties"
    weight="20"/>

The page-template itself would be very simple::

  <li id="gs-some-admin-product-link">
    <a href="/gs-some-admin-product.html">A link to some admin product</a></li>


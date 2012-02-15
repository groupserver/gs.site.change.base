Introduction
============

The base for the Change pages for a site. It provides to main 
interfaces: 

#.  The *Change Site* page, which for historical reasons lives at 
    ``/admindivision``
#.  The *Site Administration* area on the site homepage, which contains
    exactly the same things as the Change Site page.

The entire thing uses many many viewlets and viewlet managers. For both
the Change Site page and the Site Administration viewlet the structure 
is as follows::

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


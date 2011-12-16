# coding=utf-8
from zope.viewlet.interfaces import IViewletManager

class ISiteAdminStuff(IViewletManager):
    '''A viewlet manager for the stuff required to administer a site.'''
    
class ISiteAdminLinks(IViewletManager):
    '''A viewlet manager for the simple links required to administer a
     site.'''


plone4.csrffixes
================

The package aims to backport the auto CSRF implementation from Plone 5
to Plone 4.

The reason this is necessary is because there are a lot of CSRF problem
with the ZMI that Zope2 will never be able to fix.

See https://plone.org/security/hotfix/20151006
for more details.


Installation
============


Plone 4.3, 4.2, 4.1 and 4.0
---------------------------

add `plone4.csrffixes` to eggs list::

    eggs =
        ...
        plone4.csrffixes
        ...


add a new version pin for plone.protect, plone.keyring and plone.locking::

    [versions]
    ...
    plone.keyring = 3.0.1
    plone.locking = 2.0.8
    plone.protect = 3.0.16
    ...


Plone 4.0 and 4.1
-----------------

If lxml is not already included in your site, this package has a dependency
on lxml and will pull it in when installed.

We recommend pinning to version 2.3.6 of lxml. If you use a version of lxml > 3,
you'll need to also install the ``cssselect`` package. Since version
1.0.4 we require ``cssselect`` in our ``setup.py`` so it is
automatically installed.



Additional addon versions
-------------------------

To prevent some write on read errors that might cause false
positives with the auto csrf protection, these version pins have
been reported to work upgrading to::

    Products.CMFQuickInstallerTool = 3.0.12
    Products.PlonePAS = 5.0.4




Robot framework
---------------

plone4.csrffixes registers via z3c.autoinclude for Plone instances and is not
loaded in tests.

You need to include plone4.csrffixes in your package configure.zcml for it to
load in your tests::

    <include package="plone4.csrffixes" />

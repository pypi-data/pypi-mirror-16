PyLink
======

PyLink is an extensible, plugin-based IRC services framework written in
Python. It aims to be:

1) a replacement for the now-defunct Janus.

2) a versatile framework and gateway to IRC.

Support
-------

**First, MAKE SURE you've read the `FAQ <docs/faq.md>`__!**

**When upgrading between major versions, remember to read the `release
notes <RELNOTES.md>`__ for any breaking changes!**

Please report any bugs you find to the `issue
tracker <https://github.com/GLolol/PyLink/issues>`__. Pull requests are
open if you'd like to contribute, though new stuff generally goes to the
**devel** branch.

You can also find support via our IRC channels:
``#PyLink @ irc.overdrivenetworks.com``\ (`webchat <https://webchat.overdrivenetworks.com/?channels=PyLink,dev>`__)
or ``#PyLink @ chat.freenode.net``. Ask your questions and be patient
for a response.

License
-------

PyLink and any bundled software are licensed under the Mozilla Public
License, version 2.0 (`LICENSE.MPL2 <LICENSE.MPL2>`__). The
corresponding documentation in the `docs/ <docs/>`__ folder is licensed
under the Creative Attribution-ShareAlike 4.0 International License.
(`LICENSE.CC-BY-SA-4.0 <LICENSE.CC-BY-SA-4.0>`__)

Dependencies
------------

-  Python 3.4+
-  Setuptools (``pip install setuptools``)
-  PyYAML (``pip install pyyaml``)
-  `ircmatch <https://github.com/mammon-ircd/ircmatch>`__
   (``pip install ircmatch``)
-  *For the servprotect plugin*:
   `expiringdict <https://github.com/mailgun/expiringdict>`__ (note:
   unfortunately, installation is broken in pip due to
   `mailgun/expiringdict#13 <https://github.com/mailgun/expiringdict/issues/13>`__)

Supported IRCds
---------------

Primary support
~~~~~~~~~~~~~~~

These IRCds (in alphabetical order) are frequently tested and well
supported. If any issues occur, please file a bug on the issue tracker.

-  `charybdis <http://charybdis.io/>`__ (3.5+ / git master) - module
   ``ts6``
-  `InspIRCd <http://www.inspircd.org/>`__ 2.0.x - module ``inspircd``
-  `UnrealIRCd <https://www.unrealircd.org/>`__ 4.x - module ``unreal``

   -  Note: Support for mixed UnrealIRCd 3.2/4.0 networks is
      experimental, and requires you to enable a ``mixed_link`` option
      in the configuration. This may in turn void your support.

Extended support
~~~~~~~~~~~~~~~~

Support for these IRCds exist, but are not tested as frequently and
thoroughly. Bugs should be filed if there are any issues, though they
may not always be fixed in a timely fashion.

-  `Elemental-IRCd <https://github.com/Elemental-IRCd/elemental-ircd>`__
   (6.6.x / git master) - module ``ts6``
-  InspIRCd 2.2 (git master) - module ``inspircd``
-  `IRCd-Hybrid <http://www.ircd-hybrid.org/>`__ (8.2.x / svn trunk) -
   module ``hybrid``

   -  Note: for host changing support and optimal functionality, a
      ``service{}`` block / U-line should be added for PyLink on every
      IRCd across your network.

-  `juno-ircd <https://github.com/cooper/yiria>`__ (10.x / yiria) -
   module ``ts6`` (with elemental-ircd modes)
-  `Nefarious IRCu <https://github.com/evilnet/nefarious2>`__ (2.0.0+) -
   module ``nefarious``

   -  Note: Both account cloaks (user and oper) and hashed IP cloaks are
      optionally supported (HOST\_HIDING\_STYLE settings 0 to 3). Make
      sure you configure PyLink to match your IRCd settings.
   -  For optimal functionality (mode overrides in relay, etc.), a
      ``UWorld{}`` block / U-line should be added for every server that
      PyLink spawns.

Other TS6 and P10 variations may work, but are not officially supported.

Setup
-----

1) Install PyLink by using ``python3 setup.py install`` (global install)
   or ``python3 setup.py install --user`` (local install; note:
   ``--user`` is a *literal* string)

2) Rename ``example-conf.yml`` to ``pylink.yml`` and configure your
   instance there. Note that the configuration format isn't finalized
   yet - this means that your configuration may break in an update!

3) Run ``pylink`` from the command line.

4) Profit???



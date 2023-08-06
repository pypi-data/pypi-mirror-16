
Release Notes
=============

v0.4 - GTK+ 3 support
---------------------
*  Added support for *GTK+* on *Linux*.


v0.3.5 - Corrected import errors
--------------------------------
*  Propagate import errors raised on Linux to help troubleshoot missing
   ``Xlib`` module. Thanks to Lance Kindle!
*  Properly declare ``six`` as a dependency.
*  Declare ``python3-xlib`` as dependency on *Linux* for *Python 3*.


v0.3.4 - Corrected Python 3 issues on Xorg
------------------------------------------
*  Make sure that ``pystray`` can be used on *Python 3* on *Xorg*.
*  Make sure the release making script runs on *Python 3*.


v0.3.3 - Corrected encoding issues
----------------------------------
*  Make sure building works even when default encoding is not *utf-8*.
*  Corrected issue with click selector on *OSX*.


v0.3.2 - Universal wheel
------------------------
*  Make sure to build a universal wheel for all python versions.


v0.3.1 - No-change packaging update
-----------------------------------
*  Do not package an old version of ``pynput``.


v0.3 - Proper Python 3 Support
------------------------------
*  Corrected Python 3 bugs.
*  Made ``Icon.run()`` mandatory on all platforms.


v0.2 - Initial Release
----------------------
*  Support for adding a system tray icon on *Linux*, *Mac OSX* and *Windows*.



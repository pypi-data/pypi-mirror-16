Release 0.78.1 (6th August, 2016)
=================================
* Fix readthedocs versioning.
* Don't crash on ENETUNREACH.
* Various bug fixes.
* Improvements to BSD and OSX support.


Release 0.78.0 (Apr 8, 2016)
============================

* Don't force IPv6 if IPv6 nameservers supplied. Fixes #74.
* Call /bin/sh as users shell may not be POSIX compliant. Fixes #77.
* Use argparse for command line processing. Fixes #75.
* Remove useless --server option.
* Support multiple -s (subnet) options. Fixes #86.
* Make server parts work with old versions of Python. Fixes #81.


Release 0.77.2 (Mar 7, 2016)
============================

* Accidentally switched LGPL2 license with GPL2 license in 0.77.1 - now fixed.


Release 0.77.1 (Mar 7, 2016)
============================

* Use semantic versioning. http://semver.org/
* Update GPL 2 license text.
* New release to fix PyPI.


Release 0.77 (Mar 3, 2016)
==========================

* Various bug fixes.
* Fix Documentation.
* Add fix for MacOS X issue.
* Add support for OpenBSD.


Release 0.76 (Jan 17, 2016)
===========================

* Add option to disable IPv6 support.
* Update documentation.
* Move documentation, including man page, to Sphinx.
* Use setuptools-scm for automatic versioning.


Release 0.75 (Jan 12, 2016)
===========================

* Revert change that broke sshuttle entry point.


Release 0.74 (Jan 10, 2016)
===========================

* Add CHANGES.rst file.
* Numerous bug fixes.
* Python 3.5 fixes.
* PF fixes, especially for BSD.

devpi-client: commands for python packaging and testing
===============================================================

The "devpi" command line tool is typically used in conjunction
with `devpi-server <http://pypi.python.org/pypi/devpi-server>`_.
It allows to upload, test and install packages from devpi indexes.
See http://doc.devpi.net for quickstart and more documentation.

* `issue tracker <https://bitbucket.org/hpk42/devpi/issues>`_, `repo
  <https://bitbucket.org/hpk42/devpi>`_

* IRC: #devpi on freenode, `mailing list
  <https://groups.google.com/d/forum/devpi-dev>`_ 

* compatibility: {win,unix}-py{26,27,33}





Changelog
=========

2.6.4 (2016-07-15)
------------------

- fix issue337: ``devpi upload`` for packages that produce output during build
  now works.


2.6.3 (2016-05-13)
------------------

- update devpi-common requirement, so devpi-client can be installed in the same
  virtualenv as devpi-server 4.0.0.


2.6.2 (2016-04-28)
------------------

- ``devpi upload`` failed to use basic authentication and client certificate
  information.


2.6.1 (2016-04-27)
------------------

- fix issue340: basic authentication with ``devpi use`` didn't work anymore.


2.6.0 (2016-04-22)
------------------

- switching to another server with ``devpi use`` now reuses an existing
  authentication token as well as previously set basic auth and client cert.

- basic authentication is now stored at the devpi-server root instead of the
  domain root, so you can have more than one devpi-server on different paths
  with different basic auth.

- fix issue318: ``devpi test --index`` now accepts a URL, so one can test a
  package from another server without having to run ``devpi use`` first.




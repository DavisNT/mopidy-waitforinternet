****************************
Mopidy-WaitForInternet
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-WaitForInternet.svg?style=flat
    :target: https://pypi.org/project/Mopidy-WaitForInternet/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-WaitForInternet.svg?style=flat
    :target: https://pypi.org/project/Mopidy-WaitForInternet/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/github/actions/workflow/status/DavisNT/mopidy-waitforinternet/ci.yml?branch=develop&style=flat
    :target: https://github.com/DavisNT/mopidy-waitforinternet/actions/workflows/ci.yml
    :alt: GitHub Actions build status

.. image:: https://img.shields.io/coveralls/github/DavisNT/mopidy-waitforinternet.svg?style=flat
    :target: https://coveralls.io/github/DavisNT/mopidy-waitforinternet
    :alt: Coveralls test coverage

.. image:: https://img.shields.io/github/actions/workflow/status/DavisNT/mopidy-waitforinternet/servers-test.yml?branch=develop&style=flat&label=servers-test
    :target: https://github.com/DavisNT/mopidy-waitforinternet/actions/workflows/servers-test.yml
    :alt: Weekly build that tests connectivity check servers

`Mopidy <http://www.mopidy.com/>`_ extensions that wait (up to around 5 minutes) for an internet connection (and optionally for time synchronization) during early phase of Mopidy startup (before other extensions start to initialize).


Installation
============

Install by running::

    pip install Mopidy-WaitForInternet


Configuration
=============

This package consists of two Mopidy extensions - ``mopidy_waitforinternet`` (enabled by default) that waits **only** for internet connection and ``mopidy_waitfortimesync`` (disabled by default) that waits for internet connection **and** time synchronization. They have no configuration options in ``mopidy.conf`` apart from the default ``enabled`` setting::

    # To enable waiting for internet connection and time synchronization
    [waitforinternet]
    enabled = false

    [waitfortimesync]
    enabled = true

These extensions don't support proxy servers (they ignore proxy configuration in ``mopidy.conf``).

Usage
=====

Mopidy-WaitForInternet might be useful if other Mopidy extensions (e.g. extensions for online music streaming services) fail to initialize, because they try to connect to internet resources before machine running Mopidy has established an internet connection (e.g. connected to wifi) or synchronized its clock.

``mopidy_waitforinternet`` will delay initialization of other Mopidy extensions until an internet connection has been established (the extension will wait for up to around 5 minutes). It's recommended if:

* the computer running Mopidy has a `real-time clock <https://en.wikipedia.org/wiki/Real-time_clock>`_

* all of the below:

  * it is important to minimize Mopidy startup time

  * it is acceptable if other Mopidy extensions occasionally (once in several months or so) fail to initialize due to inaccurate date/time

  * the computer does not have a real-time clock

  * the computer/OS saves the time between reboots (like Raspberry Pi OS does)

  * the computer is used often

``mopidy_waitfortimesync`` will delay initialization of other Mopidy extensions until an internet connection has been established and computer's clock has been synchronized (the extension will wait for up to around 5 minutes). It's recommended if:

* prolonged Mopidy startup time is not a problem

* it is important to minimize initialization failures of other Mopidy extensions

* the computer running Mopidy does not have a real-time clock and is used rarely

Local time (computer's clock) is somewhat important for connectivity. Most internet services use HTTPS and HTTPS has certificates that are valid for a specific time period (usually 3 or 13 months). To connect to an HTTPS resource, computer's clock must be within the validity period of the HTTPS certificate used by that particular resource. Some computers (e.g. Raspberry Pi) don't have `real-time clocks <https://en.wikipedia.org/wiki/Real-time_clock>`_ and synchronize their clocks from the internet (via `NTP <https://en.wikipedia.org/wiki/Network_Time_Protocol>`_). In most cases, until the clock of such computer is synchronized it is set to the time saved at previous shutdown, for some computers the clock is set to a constant time/date (e.g. midnight January 1, 2020). As ``mopidy_waitforinternet`` uses HTTPS, it will detect internet connectivity only when computer's clock is within the validity period of the HTTPS certificate of at least one of the URLs used by ``mopidy_waitforinternet``. This guarantees that computer's clock has accuracy of a year or so, however this does not guarantee that computer's clock is accurate enough to allow connectivity (to other HTTPS resources) required by other Mopidy extensions.

Both extensions log information about the introduced startup delay.

Important internals
===================

Mopidy-WaitForInternet uses several different URLs (currently - requests to public `DoH <https://en.wikipedia.org/wiki/DNS_over_HTTPS>`_ servers) to check internet connectivity. As a future-proofing measure there is a `weekly servers-test build <https://github.com/DavisNT/mopidy-waitforinternet/actions/workflows/servers-test.yml>`_ that verifies availability of these URLs.

Time synchronization is checked by comparing local time with the ``Date`` response header of HTTP requests to the internet connectivity check URLs (difference of less than 10 seconds is considered synchronized time).

License
=======
::

   Copyright 2022-2025 Davis Mosenkovs

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Project resources
=================

- `Source code <https://github.com/DavisNT/mopidy-waitforinternet>`_
- `Issue tracker <https://github.com/DavisNT/mopidy-waitforinternet/issues>`_
- `Development branch tarball <https://github.com/DavisNT/mopidy-waitforinternet/archive/develop.tar.gz#egg=Mopidy-WaitForInternet-dev>`_
- `Weekly servers-test build that tests URLs used by Mopidy-WaitForInternet for internet connectivity check <https://github.com/DavisNT/mopidy-waitforinternet/actions/workflows/servers-test.yml>`_


Changelog
=========

v0.2.2
----------------------------------------

- Updated connectivity check URLs (switched from Quad9 to AdGuard).

v0.2.1
----------------------------------------

- Fixed build badges (including servers-test).

v0.2.0
----------------------------------------

- Added second extension (mopidy_waitfortimesync).
- Minor improvements.

v0.1.1
----------------------------------------

- Fixed README formatting.
- Initial release.

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial version.

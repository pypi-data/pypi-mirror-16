Zeroconf
================================================================================

A simple Python interface to Zeroconf service discovery and registration.
Supports python >= 2.7 <= 3.5

Installation
--------------------------------------------------------------------------------

### Requirements

The `zeroconf` module assumes that the [avahi](http://avahi.org/) command-line
tools `avahi-browse` and `avahi-publish` are available.
On Ubuntu for example, they may me installed with:

    $ sudo apt-get install avahi-utils

The module also depend on [Andrew Moffat's subprocess wrapper][sh]. Install
it with

    $ pip install sh

Read more about package install methods on Install section.

If you install the package using setup.py or pip it'll be automatically
handled so you normally don't need to do this.

[sh]: http://amoffat.github.io/sh

### Install

There are multiple methods for installing a python package.
First, download the source package, and cd to it.

Then you could directly run setup.py:

    $ python setup.py install

Or use pip, if you've got pip:

    $ pip install .


Packages can be installed system-wide (with sudo):

    $ sudo pip install .

On a virtualenv:

    $ mkvirtualenv zeroconf
    $ workon zeroconf
    $ pip install .

And with user options:

    $ python setup.py install --user

Or

    $ pip install --user .


### Running tests

Just run

    $ python setup.py test

It'll install necesary test dependences and run the tests.
Note that tests on windows are not covered this way and should be run with

    $ py.test --doctest-modules zeroconf/


Usage
--------------------------------------------------------------------------------

### Zeroconf Services Discovery

Searching for all available Zeroconf services is done by

    >>> from zeroconf import ZeroConf
    >>> zc = ZeroConf()
    >>> services = zc.search()

The search can be made more specific, for example:

    >>> services = zc.search(name=None, type="_workstation._tcp", domain="local")

The arguments, all optional, to the `search` functions are:

  - `name`: service name, defaults to `None` (interpreted as all),
  - `type`: service type, defaults to `None` (interpreted as all),
  - `domain`: domain name, defaults to `"local"`.

Search results are dictionaries:

    >>> print services
    {('tide [f0:7b:cb:42:ff:e0]', '_workstation._tcp', 'local'):
       {'txt': '', 'hostname': 'tide.local', 'port': '9', 'address': '192.168.0.13'},
     ('wreck [00:26:18:4c:3f:ee]', '_workstation._tcp', 'local'):
       {'txt': '', 'hostname': 'wreck.local', 'port': '9', 'address': '192.168.0.10'},
     ('biohazard [00:18:8b:ac:c8:45]', '_workstation._tcp', 'local'):
       {'txt': '', 'hostname': 'biohazard.local', 'port': '9', 'address': '192.168.0.12'}}

The keys are `(name, type, domain)` tuples and the values are dictionaries with `txt`,
`hostname`, `port` and `address` keys.

### Zeroconf Services Registration

Register a new zeroconf service in the local domain with:

    >>> zc = ZeroConf()
    >>> zc.register(name="ghost [08:00:27:bf:49:e1]", type="_workstation._tcp", port="9")

and when you're done, unregister it with:

    >>> zc = ZeroConf()
    >>> zc.unregister(name="ghost [08:00:27:bf:49:e1]", type="_workstation._tcp", port="9")

All arguments to `unregister` are optional, so we could have done:

    >>> zc = ZeroConf()
    >>> zc.unregister(name="ghost [08:00:27:bf:49:e1]")

or even, to unregister all services published during the Python session:

    >>> zc = ZeroConf()
    >>> zc.unregister()

Contributors
--------------------------------------------------------------------------------

  - Sébastien Boisgérault <Sebastien.Boisgerault@mines-paristech.fr>:
    initial API design, Linux/avahi support.
  - Olivier Huynh <olivierv.huynh@free.fr>: Windows/dns-sd support.
  - David Francos Cuartero <me@davidfrancos.net>: OOP rewrite, Python3 support



Prest
=====

Summary
-------

Prest is a Python library for accessing EVE Online's CREST API.

Installation
------------

From `pip <https://pip.pypa.io/en/stable/>`__:

.. code:: bash

    pip install eveprest

Use
---

Initialization
~~~~~~~~~~~~~~

.. code:: python

    from prest import Prest

    prest = Prest()

Attributes and calls
~~~~~~~~~~~~~~~~~~~~

-  Calling
-  on ``prest.Prest``: reload the base URL data

   -  ``prest()`` -> the same ``prest.Prest``

-  on ``prest.APIElement``: navigate to a new page

   -  ``prest.foo()`` -> ``prest.APIElement``

-  Getting attribute by text or item by index
-  from ``prest.Prest``: return a data subset or navigate to a new page

   -  ``prest.foo`` -> ``str``, ``int``, ``float``, ``prest.APIElement``
      of data subset, ``prest.APIElement`` to new page

-  from ``prest.APIElement``: return a data subset

   -  ``prest.foo.bar`` -> ``str``, ``int``, ``float``,
      ``prest.APIElement``

To reduce typing, ``prest.Prset.__getattr__`` combines the functionality
of ``prest.APIElement.__getattr__`` and ``prest.APIElement.__call__`` so
that calls can be made like ``prest.foo`` instead of ``prest().foo``.

If you wanted to access the X position of the Kimoto constellation, the
call would be:

.. code:: python

    prest.constellations().items.find(name='Kimotoro')().position.x

From the `base url <https://crest-tq.eveonline.com/>`__ "constellations"
is a root-level dictionary item with a "href" item, which can be called
to navigate to `that
page <https://crest-tq.eveonline.com/constellations/>`__.

From there, the ``.items`` attribute dives into the ``items`` dictionary
key and then a ``find`` method is used to get an element from the list
of dictionaries (you could loop through the items yourself, but ``find``
is for convenience). This dictionary has a "href" element, so call the
attribute to navigate
`there <https://crest-tq.eveonline.com/constellations/20000020/>`__.

Now on the final page, access the "position" key and finally its "x"
key, which is ``-134996400468185440``.

Examples
~~~~~~~~

1. Market types -> page count

.. code:: python

    prest.marketTypes().pageCount

2. "Jump Through a Wormhole" opportunity description

.. code:: python

    prest.opportunities.tasks().items.find(name='Jump Through a Wormhole').description

3. Jita 4-4 moon name

.. code:: python

    prest.systems().items.find(name='Jita')().planets[3].moons[3]().name

Using the cache
~~~~~~~~~~~~~~~

When you make a call to ``prest.foo``, the root CREST URL data stored
locally will be checked for an expired cache timer (the root URL's data
is loaded when instantiating a new ``prest.Prest`` object, you don't
need to do it manually). If it's expired, the root URL will be gotten
anew and cached. This is similar for ``prest.foo().bar().baz()`` - if
all of ``foo``, ``bar``, and ``baz`` were dictionaries with ``'href'``
keys that pointed to new pages, each would use the cache to retrieve the
page, only making a new request to CREST if the local copy of the page
is either non-existent or expired.

However, when getting attributes from a page, like
``prest.foo().bar.baz``, neither ``bar`` or ``baz`` on the page will be
using the cache. Thus, in order to make the same call multiple times
over a period of time and using the cache, either make the full
``prest.foo().bar.baz`` call again, or save the last-called element as a
local variable and call that:

.. code:: python

    foo = prest.foo

    print(foo().bar.baz)

    # later:
    print(foo().bar.baz)

    # later:
    print(foo().bar.baz)

Authentication
~~~~~~~~~~~~~~

Accessing the authenticated parts of CREST is done through
authenticating Prest:

.. code:: python

    from prest import *

    prest = Prest(client_id='', client_secret='', client_callback='')
    prest.get_authorize_url()
    auth = prest.authenticate(code)

In the code above, ``get_authorize_url`` returns a URL to redirect a web
app client to so they can log into EVE's SSO. Once they've redirected
back to your web application, pass the code in the returning URL from
EVE to the ``authenticate`` call and assign the resulting
``prest.AuthPrest`` object.

This ``prest.AuthPrest`` object works the same as the unathenticated
``prest.Prest`` object: use attributes and calls to navigate and load
CREST data, respectively.

Example of accessing a character's location:

.. code:: python

    print(auth.decode().character().location())

Refresh tokens
^^^^^^^^^^^^^^

When you authenticate for accessing CREST using a scope, Prest will get
two tokens back: the access token, which is a temporary (20 minutes)
token used for accessing CREST, and a refresh token that doesn't expire
but cannot be used to directly access CREST. When the access token
expires, Prest will get another access token from CREST using the
refresh token.

Since the refresh token doesn't expire, you'll want to keep that
somewhere safe. Prest doesn't handle this for you.

To start an authenticated session with Prest using a previously-fetched
refresh token (you can get the existing refresh token with
``prest.AuthPrest.refresh_token`` as a ``str``), do the following:

.. code:: python

    prest = Prest(client_id='', client_secret='', client_callback='')
    auth = prest.use_refresh_token('previous-refresh-token')

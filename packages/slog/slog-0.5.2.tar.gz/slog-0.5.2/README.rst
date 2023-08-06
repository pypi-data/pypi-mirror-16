Slog (simple log) is a straightforward logging framework -- (er,
library, technically, since you call it) -- that I've been using in many
school and personal projects over the past few months and that I've
decided to consolidate into a standalone package partly for great
justice and partly because I'm tired of having to copy/paste blocks of
code in and out of my old projects to use this in my new projects.

Syntax is simple enough; instantiate the Slog class and you're basically
ready to go.

::

    >>> from slog import Slog
    >>> log = Slog('myfile.log', 5)
    >>> log.ok('all systems go!')
    2015-06-11 09:19:50 || [  OK  ] ⬢  all systems go!
    >>> log.info(slog provides five levels of message importance.')
    2015-06-11 09:20:02 || [ INFO ] ⬢  slog provides five levels of message importance.
    >>> f = open('myfile.log', 'r')
    >>> for line in f: print line
    ...
    2015-06-11 09:19:50 || [  OK  ]  all systems go!
    2015-06-11 09:20:02 || [ INFO ]  slog provides five levels of message importance.

*Example with colours:*

.. figure:: https://i.imgur.com/oeF92Ee.png
   :alt: A colourful slog screenshot

   A colourful slog screenshot

(n.b. the coloured splotches don't go into the logfile -- they just show
up in the terminal during live logging for readability at a glance)

The ``Slog`` class takes two optional parameters: the name of the
logfile (defaults to ``None``) and the logging level (``[0..5]``,
defaults to ``3``). If the latter gets a parameter outside of that
range, it'll default to 3.

The levels correspond to:

-  ``5`` => log everything everywhere
-  ``4`` => log only ``info`` and higher (skips ``ok``)
-  ``3`` => log only ``warn`` and higher (skips ``ok`` and ``info``)
-  ``2`` => log only ``fail`` and higher (skips ``ok``, ``info``, and
   ``warn``)
-  ``1`` => log only ``crit``
-  ``0`` => log nothing, be quiet as the night. I don't actually know
   why I added this one. (Seriously though, it's for just to turn
   logging off easily for whatver reason.)

Writing a log entry is as simple as calling ``log.<level>()`` (with
``log`` an instance of ``Slog``) with ``<level>`` being one of
``ok``, ``info``, ``warn``, ``fail``, or ``crit``. Each of these
functions takes exactly one argument.

Because I want to retain the ability to create arbirary custom messages,
I've kept a modified ``write`` method - use it as ``log.write(message, level, color)``.
This adds even more flexibility taking int account that ``color`` can be `any` colour
supported by the ``termcolor`` package.

Changelog
=========

0.205
---

Added ``writem`` argument to all write methods. Allows the user to choose whether the output will be written to log, terminal, neither, or both, on a much more granular scale than using a global setting. **n.b.** the global setting is still supported, and there's currently no reason to discontinue it. This is purely an addition.

0.2
---

**BREAKING CHANGES!**

Per feedback, I've decided to implement the instance methods
``ok(message)``, ``info(message)``, ``warn(message)``,
``fail(message)``, ``crit(message)`` to replace the original
general-purpose ``write(message, level)``. This new, more modular layout
aims at a more consistent style.

``write(message, level=3, color='blue')`` is still available as an
instance method for customized log entries.

Installation
============

As of ``0.202``, ``pip install slog`` works for Python 2.x. The install
(and imports) seem to work for Python 3.x, but I haven't done extensive
testing and I can't guarantee anything.

Upcoming releases
=================

0.3 (ships on or before Saturday, June 13)
------------------------------------------

-  Integration with ``logging.Formatter`` from the Python STL (at least
   partially). Initially, this integration will be targeted at Python 2.x's
   ``logging.Formatter``.

0.4 (ships on or before Sunday, June 13-14)
-------------------------------------------

-  Python 3 support (assuming ``0.3``) doesn't end up supporting Python 3
   properly.

Thanks and credits
==================

-  Reddit user /u/pujuma for helping fix issue #1

-  Reddit user /u/grundee for providing feedback about the API

Slog is a simple logging framework named after the adverb some people use to
describe the task of integrating logging into their projects.

I decided to throw this together a while back as a replacement for Python's
default logger, which is unweildy and completely overkill in small projects, and
not as noob-friendly as it could be. I then stopped maintaining it because of an
influx of other responsibilities.

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



(n.b. the coloured splotches don't go into the logfile -- they just show
up in the terminal during live logging for readability at a glance.)

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
-  ``0`` => turn off logging completely on all channels

Writing a log entry is as simple as calling ``log.<level>()`` (with
``log`` an instance of ``Slog``) with ``<level>`` being one of
``ok``, ``info``, ``warn``, ``fail``, or ``crit``. Each of these
functions takes exactly one argument.

Because I want to retain the ability to create arbirary custom messages,
I've kept a modified ``write`` method - use it as ``log.write(message, level, color)``.
This adds even more flexibility taking int account that ``color`` can be `any` colour
supported by the ``termcolor`` package.

Thanks and credits
==================

-  Reddit user /u/pujuma for helping fix issue #1

-  Reddit user /u/grundee for providing feedback about the API


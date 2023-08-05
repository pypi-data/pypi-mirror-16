clop: python Command Line Option Processor
==========================================

``$ pip install clop``

``$ pydoc clop``

``$ python -m clop # Run the demo``

clop provides minimal command line option specification and processing.

When your command line processing requires the power of a king on a real horse,
use argparse in the standard python library.

When banging two coconut halves together on a stick pony is good enough,
use clop.

A single class to specify command line options,
process a command line against those options,
and make the processed results available as a dict.
Also provides a simple help string for each option and the calling program.

::

    """Your program."""

    from clop import Clop

    ...

    # Make a Clop object.
    clp = Clop()

    # Specify acceptable options and their arguments.
    clp.addOptionDef(letter = 'k',
        required = True,
        numArgs = 3,
        help = 'Help for option k')

    ...

    # optArgs is a dictionary of options and arguments
    optArgs = clp.processCmdLine(sys.argv[1:])

    ...

    # Print the help string when you need it.
    helpStr = clp.helpString('clop:\nShort demo of the clop module.')
    print(helpStr)

  clop:
  Short demo of the clop module.
  
  REQUIRED OPTIONS:
  k: Help for option k
    Allowed arguments: Exactly 3
  m: Help for option m
    Allowed arguments: Exactly 1
  n: Help for option n
    Allowed arguments: 0 or more
  
  OPTIONAL OPTIONS:
  o: Help for option o
    Allowed arguments: Exactly 0
  p: Help for option p
    Allowed arguments: Exactly 1
  q: Help for option q
    Allowed arguments: 0 or more


clop includes a demo in its main() function:

``$ python -m clop -k 1 2 3 -m one-two -n 3 4 5 -o -p 1 -q "one two"``

``{'k': ['1', '2', '3'], 'm': ['one-two'], 'o': [], 'n': ['3', '4', '5'], 'q': ['one two'], 'p': ['1']}``

- Options are a dash and a single letter: -o
- An option can be followed by zero or more arguments.
- An option can only be specified with its letter (-o). No --long options.
- An option letter can be any "letter" where letter.isalpha() is True.
- Options cannot be composed. Only one character per dash, not -olmp.
- Options can appear in any order on the command line.
- Options and arguments on the command line are strings.
  The calling program does any type and value checking and conversion
  of arguments after clop's command line processing.
  Clop makes no judgments other than allowed options and arguments.

More clop features are unlikely. If you need more, argparse is excellent,
and comes with a real horse.

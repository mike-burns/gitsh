=====
gitsh
=====

The ``gitsh`` program is an interactive shell for git. From within
``gitsh`` you can issue any git command, even using your local aliases
and configuration.

It additionally has these features:

- Informative prompt showing branch name and both color and sigil
  indicators of branch status.
- Can be used as a shebang command.
- Can read from stdin.
- Readline support.
- Inline comments.
- Can escape out to the shell.
- Load ``$VISUAL`` to write complex commands.

Installation
------------

::

    % python setup.py install

Usage
-----

::

    ~% cd gitsh
    ~/gitsh% gitsh
    master@ status -sb
    ## master
    master@ \!gvim README.md
    master@ add .
    master& commit
    master@ push


Todo
----

This commit is the initial sketch. It works for me, but there is some
that is desired. Things I want to change or add:

- Re-write in a language that exists by default on every system I use.
  This is either POSIX sh or C.
- Tests.
- Allow people to type ``git`` before the commands, by habit.
- Some sort of clever chaining of commands.
- Documentation. Manpage, Web site.
- Something to indicate whether the commit has been pushed to a remote.
- Tab completion.
- A -v flag that shows more feedback.

Author
------

Copyright 2013 Mike Burns. Licensed under BSD 3-clause license.

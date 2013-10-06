The `gitsh` program is an interactive shell for git. From within `gitsh`
you can issue any git command, even using your local aliases and
configuration.

It additionally has these features:

- Informative prompt showing branch name and both color and sigil
  indicators of branch status.
- Can be used as a shebang command.
- Can read from stdin.
- Readline support.
- Inline comments.
- Can escape out to the shell.
- Load `$VISUAL` to write complex commands.

This commit is the initial sketch. It works for me, but there is some
that is desired. Things I want to change or add:

- A `\cd` command that changes to a different git repo.
- Re-write in a language that exists by default on every system I use.
  This is either POSIX sh or C.
- Tests.
- Allow people to type `git ` before the commands, by habit.
- Some sort of clever chaining of commands, to express e.g. "add every
  file not already added within the `bin/` directory".
- Documentation. Manpage, Web site.
- Something to indicate whether the commit has been pushed to a remote.

Author

Copyright 2013 Mike Burns. Licensed under BSD 3-clause license.

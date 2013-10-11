import sys
import os
import readline
from .runner import Gitsh, InteractiveGitsh


def interactive():
    return os.isatty(sys.stdin.fileno()) and len(sys.argv) == 1

def main():
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind('bind ^I rl_complete')

    if interactive():
        InteractiveGitsh().cmdloop()
    elif len(sys.argv) > 1:
        fh = open(sys.argv[1])
        Gitsh(None, stdin=fh).cmdloop()
        fh.close()
    else:
        Gitsh().cmdloop()

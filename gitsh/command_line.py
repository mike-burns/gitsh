import sys
import os
import readline
from .runner import Gitsh
from .completer import Completer


def interactive():
    return os.isatty(sys.stdin.fileno()) and len(sys.argv) == 1

def main():
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind('bind ^I rl_complete')

    program = Gitsh()
    if interactive():
        program.complete = Completer()
        program.cmdloop()
    elif len(sys.argv) > 1:
        fh = open(sys.argv[1])
        program.stdin = fh
        program.use_rawinput = False
        program.cmdloop()
        fh.close()
    else:
        program.cmdloop()


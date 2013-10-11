import readline
import subprocess
import re


class Completer(object):
    """
    Callable object that provides readline tab completion for git commands.
    """

    @classmethod
    def register(cls):
        """
        Registers an instance of Completer as the readline completer, and binds
        the tab key to complete in a way that is compatible with both
        GNU readline and libedit.
        """
        if 'libedit' in readline.__doc__:
            readline.parse_and_bind('bind ^I rl_complete')
        else:
            readline.parse_and_bind('tab: complete')
        readline.set_completer(cls())

    def __call__(self, text, n):
        """
        Behaves as a readline completion function (that is, given text and n,
        it returns the nth possible completion beginning with text)
        """
        competions = self._competions_for(text)
        if n < len(competions):
            return competions[n]
        else:
            return None

    def _competions_for(self, text):
        return filter(lambda s: s.startswith(text), self._git_commands())

    def _git_commands(self):
        """
        Returns all possible git commands, as listed by `git help -a`. This is
        based on the official git bash completion script.
        """
        if not hasattr(self, '_commands'):
            matcher = re.compile(r'^  [^ ]')
            splitter = re.compile(r'\s+')
            self._commands = set()
            output = subprocess.check_output(('/usr/bin/env', 'git', 'help', '-a'))
            for line in output.splitlines():
                if matcher.match(line):
                    map(self._commands.add, splitter.split(line.strip()))
        return self._commands

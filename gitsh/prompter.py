import re
import os


class Prompter(object):
    def make_prompt(self):
        (branch, clean) = self._git_status()
        prompt = self._prompt_format().replace('%c', self._prompt_color(clean)).replace('%w', self._prompt_reset_color()).replace('%b', branch).replace('%#', self._prompt_terminator(clean)).replace('%d', os.getcwd()).replace('%D', os.path.basename(os.getcwd()))
        return prompt


    def _prompt_format(self):
        """
        %c - start coloring based on status
        %w - stop coloring based on status
        %b - branch name
        %# - prompt terminator, changes based on status
        %d - current directory, absolute
        %D - current directory, just basename
        """
        return "%b%c%#%w "

    def _git_status(self):
        status = os.popen('git status 2>&1').read()
        if re.search("Not a git repository", status):
            return ('uninitialized', 'uninitialized')
        elif re.search("Not currently on any branch", status):
            return ('(no branch)', 'no-branch')

        branch = re.search("On branch (.*)", status).group(1)

        if re.search("working directory clean", status):
            return (branch, 'clean')
        elif re.search("[uU]ntracked files", status):
            return (branch, 'untracked')
        elif re.search("Changes to be committed", status):
            return (branch, 'added')
        elif re.search("deleted:", status):
            return (branch, 'deleted')
        elif re.search("modified:", status):
            return (branch, 'modified')

    def _prompt_color(self, clean):
        return {'clean': "\033[00m",
                'untracked': "\033[00;31m",
                'added': "\033[00;33m",
                'deleted': "\033[00;33m",
                'modified': "\033[00;33m",
                'uninitialized': "\033[00;41m",
                'no-branch': "\033[00;34m",
                }[clean]

    def _prompt_reset_color(self):
        return "\033[00m"

    def _prompt_terminator(self, clean):
        return {'clean': '@',
                'untracked': '!',
                'added': '&',
                'deleted': '&',
                'modified': '&',
                'uninitialized': '!!',
                'no-branch': '*'}[clean]

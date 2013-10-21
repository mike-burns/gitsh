import subprocess
import tempfile
import cmd
import os
from .prompter import Prompter
from .completer import Completer


class Gitsh(cmd.Cmd):
    prompt = ''
    use_rawinput = False

    def precmd(self, line):
        if line == 'EOF' or line == '':
            return line
        elif line.startswith("\\"):
            name = self._backslash_command_line(line[1])
            return "backslash_%s %s" % (name, line[2:])
        else:
            return "git_command %s" % line

    def do_EOF(self, _line):
        print
        return True

    def do_backslash_editor(self, _line):
        (fd, pathname) = tempfile.mkstemp(suffix='sh')
        fh = os.fdopen(fd)
        prior_stdin = self.stdin
        prior_rawinput = self.use_rawinput
        prior_prompt = self.prompt
        try:
            subprocess.call("%s %s" % (self._get_editor(), pathname), shell=True)
            self.stdin = fh
            self.use_rawinput = False
            self.prompt = ''
            self.cmdloop()
        except OSError as e:
            print >>sys.stderr, e
        finally:
            self.stdin = prior_stdin
            self.use_rawinput = prior_rawinput
            self.prompt = prior_prompt
            fh.close()
            os.unlink(pathname)

    def do_shell(self, line):
        try:
            if line == "":
                subprocess.call("%s -i" % self._get_shell(), shell=True)
            else:
                subprocess.call("%s -c '%s'" % (self._get_shell(), line), shell=True)
        except OSError as e:
            print >>sys.stderr, e

    def do_backslash_shell(self, line):
        return self.do_shell(line)

    def do_help(self, _line):
        print "\\!\trun shell"
        print "\\?\tshow this help"
        print "\\\"\twrite a string"
        print "\\c\tchange directory"
        print "\\e\topen editor"
        print "\\h\tshow help for a give topic"
        print "\\q\tquit"

    def do_backslash_help(self, line):
        return self.do_help(line)

    def do_backslash_git_help(self, topic):
        try:
            subprocess.call("git --help %s" % topic, shell=True)
        except OSError as e:
            print >>sys.stderr, e

    def do_backslash_quit(self, _line):
        return True

    def do_backslash_change_dir(self, directory):
        if directory == "":
            print os.getcwd()
        else:
            os.chdir(os.path.expanduser(directory.strip()))

    def do_backslash_string(self, string):
        print string.rstrip('"')

    def do_git_command(self, line):
        try:
            subprocess.call("git %s" % line, shell=True)
        except OSError as e:
            print >>sys.stderr, e

    def default(self, line):
        return self.do_git_command(line)

    def _get_editor(self):
        output = subprocess.check_output(('/usr/bin/env', 'git', 'var', 'GIT_EDITOR'))
        return output.splitlines()[0]

    def _get_shell(self):
        return os.environ.get('SHELL') or 'sh'

    def _backslash_command_line(self, flag):
        return {'e': 'editor',
                '!': 'shell',
                '?': 'help',
                'h': 'git_help',
                'q': 'quit',
                'c': 'change_dir',
                '"': 'string'}[flag]


class InteractiveGitsh(Gitsh):
    complete = Completer()
    use_rawinput = True

    def preloop(self):
        self._set_prompt()

    def postcmd(self, stop, line):
        if not stop:
            self._set_prompt()
        return stop

    def emptyline(self):
        return self.do_git_command("status")

    def _set_prompt(self):
        prompter = Prompter()
        self.prompt = prompter.make_prompt()

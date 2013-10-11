from unittest import TestCase

from gitsh.prompter import Prompter

class TestPrompter(TestCase):
    def test_whatever(self):
        p = Prompter()
        self.assertEqual(p.make_prompt(), "whatever")

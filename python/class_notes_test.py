import unittest

# -*- coding: utf-8 -*-
# To use, at the directory you saved this:
# python -m unittest test_stdio

import sys
import io
import unittest


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)


def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = StringIO()
    sys.stdout = StringIO()


class StdioTestCase(unittest.TestCase):

    def test_example(self):
        stub_stdin(self, '42')
        stub_stdouts(self)
        example()
        self.assertEqual(sys.stdout.getvalue(), '42\n')

    def helper(self, data, answer, runner):
        stub_stdin(self, data)
        stub_stdouts(self)
        runner()
        self.assertEqual(sys.stdout.getvalue(), answer)
        # self.doCleanups()  # optional, see comments below

    def test_various_inputs(self):
        data_and_answers = [
            ('hello', 'HELLOhello'),
            ('goodbye', 'GOODBYEgoodbye'),
        ]

        runScript = upperlower  # the function I want to test

        for data, answer in data_and_answers:
            self.helper(data, answer, runScript)


class StringIO(io.StringIO):
    """
    A "safely" wrapped version
    """

    def __init__(self, value=''):
        value = value.encode('utf8', 'backslashreplace').decode('utf8')
        io.StringIO.__init__(self, value)

    def write(self, msg):
        io.StringIO.write(self, msg.encode(
            'utf8', 'backslashreplace').decode('utf8'))


def example():
    number = raw_input()
    print number.upper()


def upperlower():
    raw = raw_input()
    print(raw.upper() + raw),


# Calling doCleanup is optional simply because TestCase will call it by
# default.  It's there to clean up instantly if it is desired and won't
# invoke other cleanup code prematurely.

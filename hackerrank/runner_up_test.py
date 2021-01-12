import unittest
from runner_up import score_runner_up
import io
from unittest import mock


class RunnerUpTest(unittest.TestCase):
    def test_simple(self):
        with mock.path('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            score_runner_up(5, [2, 3, 6, 6, 5])
            assert mock_stdout.getvalue() == 5


if __name__ == '__main__':
    unittest.main()

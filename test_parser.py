from parser import parser
import unittest
import io
import contextlib
from pathlib import Path

"""
Tests:
    - Type validation
    - Required/missing argument validation
    - Mutual exclusivity or conflict checks
    - Value constraints (e.g. allowed ranges, formats)
    - Integration between options
"""
class TestParserGeneralOptions(unittest.TestCase):
    def test_valid_name_arg(self):
        cases = [
            (["contest", "-i", "1", "-m", "Round13"], "Round13"),
            (["quick", "-m", "Problem N. 2"], "Problem N. 2"),
            (["contest", "-i", "1", "--name", "KeroContest"], "KeroContest"),
            (["quick", "--name", "Quick Problem"], "Quick Problem"),
        ]
        for case in cases:
            args = parser.parse_args(case[0])
            self.assertEqual(args.name, case[1])

    def test_valid_path_arg(self):
        cases = [
            (["contest", "-i", "1", "-p", "./ps/cf"], Path("ps/cf")),
            (["quick", "-p", "/ps/cf"], Path("/ps/cf")),
            (["contest", "-i", "1", "--path", "/kero/wagdy/"], Path("/kero/wagdy")),
            (["quick"], Path(".")),
        ]
        for case in cases:
            args = parser.parse_args(case[0])
            self.assertEqual(args.path, case[1])

class TestParserContest(unittest.TestCase):
    def test_valid_args(self):
        """valid args shouldn't raise any error"""
        cases = [
            ("contest -n 5", "n", 5),
            ("contest -i 24", "id", 24),
            ("contest --to f", "to", "F"),
            ("contest --id 89", "id", 89),
        ]
        for case in cases:
            args = parser.parse_args(case[0].split())
            self.assertEqual(getattr(args, case[1]), case[2])


    def test_invalid_types(self):
        """invalid args types should raise SystemExit"""
        cases = [
            "contest -n f", # f is not number of problems
            "contest -i abc", # abc is not contestId
            "contest --to 2", # 2 is not a single letter
        ]
        for case in cases:
            with self.assertRaises(SystemExit):
                with contextlib.redirect_stderr(io.StringIO()): # redirect the stderr to dummy string stream
                    parser.parse_args(case.split())

class TestParserArgumentsExclusivity(unittest.TestCase):
    def test_multiple_subcommand_raise_error(self):
        cases = [
            "contest goto -i 2", 
            "contest quick -m Lol", 
            "goto quick",
        ]

        for case in cases:
            with self.assertRaises(SystemExit):
                with contextlib.redirect_stderr(io.StringIO()): # redirect the stderr to dummy string stream
                    parser.parse_args(case.split())

    def test_multiple_contest_group_options_raise_error(self):
        cases = [
            "contest -i 2 -n 5", 
            "contest -i 5 --to F", 
            "contest --to F -n 4",
        ]

        for case in cases:
            with self.assertRaises(SystemExit):
                with contextlib.redirect_stderr(io.StringIO()): # redirect the stderr to dummy string stream
                    parser.parse_args(case.split())

    def test_multiple_goto_group_options_raise_error(self):
        cases = [
            "goto -l F -n", 
            "goto -n -p", 
            "goto -p --next",
            "goto --prev -l F",
        ]

        for case in cases:
            with self.assertRaises(SystemExit):
                with contextlib.redirect_stderr(io.StringIO()): # redirect the stderr to dummy string stream
                    parser.parse_args(case.split())


if __name__ == '__main__':
    unittest.main()
from parser import parser
import unittest
import io
import contextlib



class TestParserContest(unittest.TestCase):
    def test_equality(self):
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
        cases = [
            "contest -n f", # f is not number of problems
            "contest -i abc", # abc is not contestId
            "contest --to 2", # 2 is not a single letter
            "contest --id -1", # -1 is not a valid contestId
        ]
        for case in cases:
            with self.assertRaises(SystemExit):
                with contextlib.redirect_stderr(io.StringIO()): # redirect the stderr to dummy string stream
                    parser.parse_args(case.split())


if __name__ == '__main__':
    unittest.main()
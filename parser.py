import argparse
from custom_types import single_letter, contest_id, problems_count
from pathlib import Path

parser = argparse.ArgumentParser(prog="cf", description="Command for Codeforces Competitve Programmers")

subparsers = parser.add_subparsers()

parser_contest = subparsers.add_parser("contest", help="Creats contest problems")
parser_quick = subparsers.add_parser("quick", help="Create a quick problem folder")
parser_goto = subparsers.add_parser("goto", help="Navigator")
parser_another = subparsers.add_parser("another", help="Creates another solution folder for current problem")

# ---------------------
for curr_parser in [parser_contest, parser_quick, parser_another]:
    curr_parser.add_argument("--name", "-m",
                        help="Write the contest/problem name (default: %(default)s)",
                        type=str,
                        default="A Contest",
    )
    curr_parser.add_argument("--path", "-p",
                        help="Specify contest/problem path (default: %(default)s)",
                        type=Path,
                        default=".",
    )
    curr_parser.add_argument("--template", "-t",
                        help="Create problem files with code snippet template",
                        action="store_true"
    )

    curr_parser.add_argument("--file-in-out", "--fio",
                        help="Creates input.txt & output.txt files with each problem file",
                        action="store_true"
    )

# ---------------------
contest_group = parser_contest.add_mutually_exclusive_group(required=True)
contest_group.add_argument("--id", "-i",
                        help="Proivde the contest id to get number of problems easily from it",
                        type=contest_id
)
contest_group.add_argument("--to",
                        help="Provide the last problem letter (if contest has 3 problems, provide the letter c)",
                        type=single_letter
)
contest_group.add_argument("-n",
                        help="Provide the number of problems in the contest",
                        type=problems_count
)
# ---------------------

# ---------------------
goto_group = parser_goto.add_mutually_exclusive_group(required=True)
goto_group.add_argument("--letter", "-l",
                        help="Go to problem of the provided letter",
                        type=single_letter,
)
goto_group.add_argument("--next",
                        help="Go to the next problem",
                        action="store_true"
)
goto_group.add_argument("--prev",
                        help="Go to the next problem",
                        action="store_true"
)
# ---------------------

# Import parser from this file and call parser.parse_args()
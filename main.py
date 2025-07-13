# main.py
from parser import parser
from create_problem import create_problem
from create_contest import create_contest
from goto_problem import goto_problem
import os
import subprocess
from pathlib import Path

def main():
    args = parser.parse_args()
    if args.subcommand == "contest":
        n_problems = 1
        if args.n:
            n_problems = args.n
        elif args.to:
            n_problems = ord(args.to) - ord('A') + 1
        elif args.id:
            # TODO fetch
            pass

        # TODO get defaults from config
        name = args.name
        path: Path = args.path
        templated = args.template
        fio = args.file_in_out

        create_contest(name, path, n_problems, templated, fio)
        
        contest_path = path.joinpath("/" + name + "/")
        goto_problem("A", contest_path)
        # TODO goto first problem

    elif args.subcommand == "quick":

        # TODO get defaults from config
        name = args.name
        path = args.path
        templated = args.template
        fio = args.file_in_out

        create_problem(name, path, templated, fio)
        # TODO goto first problem


    elif args.subcommand == "goto":
        problem_name = 'A'
        curr_problem = os.getcwd().split(os.path.sep)[-1]
        if args.letter:
            problem_name = args.letter
        elif args.next:
            problem_name = chr(ord(curr_problem) + 1)
        elif args.prev:
            problem_name = chr(ord(curr_problem) - 1)

        goto_problem(problem_name)

    elif args.subcommand == "another":
        # TODO
        pass

if __name__ == '__main__':
    main()
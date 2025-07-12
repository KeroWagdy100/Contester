#create_contest.py
from create_problem import create_problem
from pathlib import Path
import os

def create_contest(name: str,
                   path: Path,
                   n_problems: int,
                   templated: bool,
                   fio: bool
    ):
    folder_path = os.path.join(path, name)
    try:
        os.makedirs(folder_path)
    except FileExistsError as err:
        print(f"File Exists Error: {err}")
    for i in range(0, n_problems):
        char = chr(ord('A') + i)
        create_problem(char, folder_path, templated, fio)
    print(f"Created Contest {name} problems from A to {chr(ord('A') + n_problems-1)} successfully")

if __name__ == '__main__':
    create_contest("Contest Example", "./testing", 5, True, True)

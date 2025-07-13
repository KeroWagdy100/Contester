import os
import pyperclip
from pathlib import Path


def goto_problem(problemName, contest_path = Path()):
    # os.chdir(pth)
    # subprocess.run(["code", pth + "/" + problemName + ".cpp"])
    # command = f"cd {pth}; code {problemName + ".cpp"}"
    # pyperclip.copy(command)
    # print(f"command ({command}) copied! just paste + Enter")
    pass

if __name__ == '__main__':
    goto_problem("A")

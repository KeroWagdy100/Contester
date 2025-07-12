import os
import subprocess


def goto_problem(problemName):
    curr_folder = os.curdir.split(os.path.sep)[-1]
    pth = ""
    if (curr_folder.isalpha()):
        pth = "../" + problemName
    else:
        pth = "./" + problemName

    os.chdir(pth)
    # subprocess.run(["code", pth + "/" + problemName + ".cpp"])
    print(pth + "/" + problemName + ".cpp")

if __name__ == '__main__':
    goto_problem("A")

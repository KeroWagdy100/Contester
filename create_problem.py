import os
import subprocess
from pathlib import Path 

def create_problem(name: str,
                   path: Path,
                   templated: bool,
                   fio: bool
    ):
    """
    Create a problem folder with needed files
    * [name].cpp => main src code file
    * input.txt => if(fio)
    * output.txt => if(fio)
    """
    folder_path = os.path.join(path, name)
    try:
        os.makedirs(folder_path)
    except FileExistsError as err:
        print(f"File Exists Error: {err}")
    

    with open(os.path.join(folder_path, name + ".cpp"), mode='w') as f:
        if templated:
            f.write("Template")
    if fio:
        open(os.path.join(folder_path, "input.txt"), "w")
        open(os.path.join(folder_path, "output.txt"), "w")

if __name__ == '__main__':
    create_problem("A", "./testing", True, True)
    create_problem("B", "./testing", True, True)

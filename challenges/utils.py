import os
from subprocess import run

__all__ = ["init", "zip"]

def init():
    if "testcases/" not in os.listdir():
        os.mkdir("testcases/")

    files = os.listdir("testcases/")
    if not ("input" in files and "output" in files):
        os.mkdir("testcases/input/")
        os.mkdir("testcases/output/")
        print("Created Directories")


def zip(name: str):
    """Creates testcases zip file."""

    os.chdir("testcases/")
    zipping = run(f"zip -qr {name}_testcases.zip input/ output/", shell=True, text=True)

    if f"{name}_testcases.zip" in os.listdir() and not zipping.stderr:
        print("Zipping Successful!!")
    else:
        print(f"Zipping Failed!!")

    os.chdir("../")


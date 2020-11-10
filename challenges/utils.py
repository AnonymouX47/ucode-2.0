import os
from time import perf_counter
from subprocess import run
import functools

__all__ = ["init", "zipper", "timer", "worst_case"]

def init():
    if "testcases" not in os.listdir():
        os.mkdir("testcases/")

    files = os.listdir("testcases/")
    if not ("input" in files and "output" in files):
        os.mkdir("testcases/input/")
        os.mkdir("testcases/output/")
        print("Created Directories")
    else:
        run("rm -r testcases/*put/*", shell=True)


def zipper(name):
    """Creates testcases zip file."""

    os.chdir("testcases/")
    zipping = run(f"zip -qr {name}_testcases.zip input/ output/", shell=True, text=True)

    if f"{name}_testcases.zip" in os.listdir() and not zipping.stderr:
        print("Zipping Successful!!")
    else:
        print(f"Zipping Failed!!")

    os.chdir("../")


def timer(func):
    """Simple timer function decorator"""

    @functools.wraps(func)
    def wrapper(*args):
        start = perf_counter()
        result = func(*args)
        duration = perf_counter() - start
        if duration > worst["time"]:
            worst["args"], worst["result"], worst["time"] = args, result, duration
        return result

    return wrapper


def worst_case():
    for item in worst.items():
        print(*item, sep=': ')
        print()


worst = {"args": None, "result": None, "time": 0}

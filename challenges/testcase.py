""" Runs a single test case using evaluate.evaluate()
    "evaluated" by test.py per testcase
"""

from evaluate import evaluate

challenge = input()
filename = input()

print(evaluate("python solution.py",
                open(f"{challenge}/testcases/input/{filename}"),
                wd=f"./{challenge}/"))

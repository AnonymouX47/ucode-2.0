#! /usr/bin/env python3

""" Runs a single test case using evaluate.evaluate()
    "evaluated" by test.py per testcase
"""

import sys
import os
from evaluate import evaluate

challenge = sys.argv[1]
results = {}

for filename in sorted(os.listdir(f"{challenge}/testcases/input/"),
                        key=lambda s :s[-6:]):
    output = evaluate("python testcase.py", text=f"{challenge}\n{filename}")
    results[filename] = eval(output[2])

print("Worst Case: {}\n{}".format(*max(results.items(), key=lambda t :t[1][0])))
print()

if len(sys.argv) > 2:
    for result, filename in zip(results.values(),
                                sorted(os.listdir(f"{challenge}/testcases/output/"),
                                        key=lambda s :s[-6:])):
        for lineno, line1, line2 in zip(range(1, 1000), result[2].split('\n'),
                                open(f"{challenge}/testcases/output/{filename}")):
            if line1 != line2.rstrip('\n'):
                print(f"Unmatching output in {filename} at line {lineno}:")
                print(f"{line1} != {line2}")

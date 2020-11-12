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

if "print" in sys.argv:
    print(*map("{0[0]}: {0[1]}".format, results.items()), sep='\n')
    print()

if "profile" in sys.argv:
    print("Total Time: %.2f" % sum([res[1][0] for res in results.items()]))
    print("Total Space: %i\n" % sum([res[1][1] for res in results.items()]))
    print("Worst Time: {0}\n{1[0]}\n".format(*max(results.items(), key=lambda t :t[1][0])))
    print("Worst Space: {0}\n{1[1]}\n".format(*max(results.items(), key=lambda t :t[1][1])))

if "check" in sys.argv:
    for result, filename in zip(results.values(),
                                sorted(os.listdir(f"{challenge}/testcases/output/"),
                                        key=lambda s :s[-6:])):
        for lineno, line1, line2 in zip(range(1, 1000), result[2].split('\n'),
                                open(f"{challenge}/testcases/output/{filename}")):
            if line1 != line2.rstrip('\n'):
                print(f"Unmatching output in {filename} at line {lineno}:")
                print(f"{line1} != {line2}")

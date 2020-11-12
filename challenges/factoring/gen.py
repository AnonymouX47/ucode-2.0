#! /usr/bin/env python3

import sys
from random import randint
from solution import solve

sys.path.append("../")
from utils import *

init()

i = 0
# Sample
t, p = 2, 4
testcases = ((13195, 14300, 195, 20),
            (195, 14300, 20, 26390))
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{} {}\n{}".format(t, p,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, map(solve, testcases)))))

# Random
for n_lim in (1000, 1000000, 1000000000, 1000000000000):
    for _ in range(4):  # 2 main testcases per limit.
        i += 1
        t, p = randint(1, 10), randint(2, 20)
        testcases = [[randint(1, n_lim) for _ in range(p)] for _ in range(t)]
        with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
            in_file.write("{} {}\n{}".format(t, p,
            '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
            out_file.write("{}".format('\n'.join(map(str, map(solve, testcases)))))


zipper()


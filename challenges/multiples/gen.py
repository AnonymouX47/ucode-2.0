#! /usr/bin/env python3

import sys
from random import choice, randint
from itertools import starmap
from solution import solve

sys.path.append("../")
from utils import *

init()

i = 0
# Sample
t, testcases = 2, ((3, 5, 10), (7, 8, 1000))
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}".format(t,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, starmap(solve, testcases)))))

# Random
prev_n_lim = 1
for n_lim in (100, 1000, 100000, 10000000, 1000000000):
    for t_lim in (100, 1000, 10000, 100000):
        i += 1
        t = randint(1, t_lim)
        a = randint(3, 20)
        while a == (b := randint(3, 20)): pass
        testcases = [[a, b, randint(prev_n_lim, n_lim)] for _ in range(t)]
        with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
            in_file.write("{}\n{}".format(t,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
            out_file.write("{}".format('\n'.join(map(str, starmap(solve, testcases)))))
    prev_n_lim = n_lim

# Targeted
## N <= min(A, B) (Output === 0)
i += 1
t = 100
testcases = []
for _ in range(t):
    a = randint(3, 20)
    while a == (b := randint(3, 20)): pass
    testcases.append((a, b, randint(1, min(a, b))))
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}".format(t,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, starmap(solve, testcases)))))

## Should be Worst case
i += 1
t = 99999
# Primes have lowest LCMs since GCDs are 1, hence max possible number of multiples
primes = (3, 5, 7, 11, 13, 17, 19)
a = choice(primes)
while a == (b := choice(primes)): pass
testcases = [(a, b, randint(1000000, n_lim)) for _ in range(t)]
testcases.append((3, 5, 1000000000))
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}".format(t,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, starmap(solve, testcases)))))



zipper()


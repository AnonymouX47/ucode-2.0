#! /usr/bin/env python3

import sys
from random import choice, randint, sample, shuffle
from solution import solve

sys.path.append("../")
from utils import *

init()

i = 0
# Sample
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    n = 9
    a = [3,3,4,4,5,9,7,6,11]
    in_file.write(f"{n}\n{' '.join(str(i) for i in a)}\n")
    out_file.write(f"{solve(a)}\n")


# Random
for t, w, x in ((10, 2, 30), (5, 31, 70), (5, 71, 100)):
    j = 0
    while j < t:
        i += 1
        j += 1
        # Choose random array size where w <= n <= x
        n = randint(w, x)

        # Randomly pick k distinct integers in a certain range(0, x+1)
        # where 1 <= k <= n
        d = sample(range(x+1), randint(1, n))

        # Populate actual array with n random picks from list of distinct integers
        a = [choice(d) for _ in range(n)]
        shuffle(a)

        # To satisfy given constraint
        if solve(a) < 2:
            print(n, a)
            j -= 1
            i -= 1
            continue

        with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
            in_file.write(f"{n}\n{' '.join(str(i) for i in a)}\n")
            out_file.write(f"{solve(a)}\n")


# Targeted
## Singular population
i += 1
n = 100
a = [randint(0, 101)] * n
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write(f"{n}\n{' '.join(str(i) for i in a)}\n")
    out_file.write(f"{solve(a)}\n")

## Greatest integer in discrete set is the one with largest subset.
i += 1
n = 100
a = [randint(0, 10) for _ in range(40)] + [15]*60
shuffle(a)
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write(f"{n}\n{' '.join(str(i) for i in a)}\n")
    out_file.write(f"{solve(a)}\n")

## Last two greatest integers in discrete set make the largest subset.
i += 1
n = 100
a = [randint(0, 10) for _ in range(40)] + [15]*35 + [17]*25
shuffle(a)
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write(f"{n}\n{' '.join(str(i) for i in a)}\n")
    out_file.write(f"{solve(a)}\n")


zipper("")


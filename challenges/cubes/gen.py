#! /usr/bin/env python3

import sys
from random import randint
from solution import solve

sys.path.append("../")
from utils import *

init()

i = 0
# Sample
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("2\n3 200\n27 125")
    out_file.write(f"{solve(3, 200)}\n{solve(27, 125)}")

# Random cases
ranges = ((1, 10), (100, 1000), (10000, 100000), (1000000, 10000000), (100000000, 1000000000))

for a_range in range(len(ranges)):
    for b_range in range(a_range, len(ranges)):
        i += 1

        with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
            t = randint(1, 100)
            in_file.write(f"{t}\n")

            for _ in range(t):
                a = randint(*ranges[a_range])
                if a_range == b_range:
                    b = randint(a, ranges[b_range][1])
                else:
                    b = randint(*ranges[b_range])
            
                in_file.write(f"{a} {b}\n")
                out_file.write(f"{solve(a, b)}\n")

# Cubes only
i += 1
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("30\n")
    for tup in ((5, 1, 10), (10, 50, 100), (15, 100, 500)):
        for _ in range(tup[0]):
            a = randint(tup[1], tup[2])
            b = randint(a, tup[2])

            a, b = a**3, b**3

            in_file.write(f"{a} {b}\n")
            out_file.write(f"{solve(a, b)}\n")

# Edge cases
i += 1
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("8\n")
    in_put = """1 1
1000000000 1000000000
512 512
1 1000000000
1 999999999
27 45
800 1000
65 124"""

    in_file.write(in_put)
    for line in in_put.split('\n'):
        out_file.write("{}\n".format(
                            solve(*[int(x) for x in line.strip().split(' ')])))


zipper("cubes")


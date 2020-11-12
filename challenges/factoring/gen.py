#! /usr/bin/env python3

import sys
from math import sqrt
from random import choice, randint, sample
from solution import solve

sys.path.append("../")
from utils import *


def isprime(n):
    if not n & 1 or n == 1: return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if not n % i: return False

    return True


init()

i = 0
# Sample
t, p = 2, 4
testcases = ((13195, 14300, 195, 20),
            (195, 13195, 20, 26390))
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{} {}\n{}".format(t, p,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, map(solve, testcases)))))

# Random
for n_lim in (1000, 1000000, 1000000000, 1000000000000):
    for _ in range(4):  # 4 main testcases per limit.
        i += 1
        t, p = randint(1, 10), randint(2, 20)
        testcases = [[randint(1, n_lim) for _ in range(p)] for _ in range(t)]
        with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
            in_file.write("{} {}\n{}".format(t, p,
            '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
            out_file.write("{}".format('\n'.join(map(str, map(solve, testcases)))))

# Targeted

## Low
primes = [i for i in range(101, 1000, 4) if isprime(i)]
i += 1
t, p = 2, 20
testcases = (sample(primes, 20),
            (choice(primes),) * 20)

with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{} {}\n{}".format(t, p,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, map(solve, testcases)))))


## Mid
primes = [int(i) for i in open("primes.txt").read().rstrip(' ').split(' ')]
i += 1
t, p = 2, 15
testcases = (sample(primes, 15),
            (choice(primes),) * 15)

with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{} {}\n{}".format(t, p,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, map(solve, testcases)))))

## Large (Not primes)
i += 1
t, p = 1, 3
testcases = ((900000900009, 9000090009, 90009009),)

with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{} {}\n{}".format(t, p,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, map(solve, testcases)))))

## Multiples
i += 1
t, p = 1, 7
testcases = (sample((13, 29, 13195, 26390, 39585, 65975, 79170, 620165), 7),)

with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{} {}\n{}".format(t, p,
        '\n'.join(map(' '.join, (map(str, testcase) for testcase in testcases)))))
    out_file.write("{}".format('\n'.join(map(str, map(solve, testcases)))))



zipper()


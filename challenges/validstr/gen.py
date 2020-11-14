#! /usr/bin/env python3

import sys
from random import choice, choices, randint, shuffle
from string import ascii_lowercase as letters
from solution import solve

sys.path.append("../")
from utils import *

init()

i = 0
# Sample
t = 4
testcases = ("abcd", "aabbccc", "aabbbccc", "zywxyzwzzxyy")
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write(f"{t}\n")
    for testcase in testcases:
        in_file.write(f"{testcase}\n")
    for testcase in testcases:
        out_file.write(f"{solve(testcase)}\n")


# Random
last = 1
for s_lim in (10, 100, 1000, 10000, 100000):
    for _ in range(4):
        i += 1
        t = randint(1, 100)
        testcases = [''.join(choices(letters, k=randint(last, s_lim))) for _ in range(t)]
        with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
            in_file.write(f"{t}\n")
            for testcase in testcases:
                in_file.write(f"{testcase}\n")
            for testcase in testcases:
                out_file.write(f"{solve(testcase)}\n")
    last = s_lim


#Targeted
i += 1
t = 11
testcases = [choice(letters) * 100000]  # YES

s = list(letters[:-1] * 3000 + 'z')  # YES -(z)
shuffle(s)
testcases.append(''.join(s))
s = list(letters[:-1] * 3000 + "zz")  # YES -(zz)
shuffle(s)
testcases.append(''.join(s))
s = list('a' * 10000 + 'bcd' * 9999)  # YES -(a)
shuffle(s)
testcases.append(''.join(s))
s = list('abc' * 10000 + 'd' * 9999)  # NO
shuffle(s)
testcases.append(''.join(s))
s = list('a' * 10001 + 'bcd' * 9999)  # YES -(aa)
shuffle(s)
testcases.append(''.join(s))
s = list('ab' * 10000 + 'cd' * 9999)  # YES -(ab)
shuffle(s)
testcases.append(''.join(s))
s = list(letters[:-2] * 4000 + 'yz')  # YES -(yz)
shuffle(s)
testcases.append(''.join(s))
s = list(letters[:-2] * 3000 + 'yz' * 3001)  # YES -(yz)
shuffle(s)
testcases.append(''.join(s))
s = list('a' + letters[1:-1] * 3000 + 'z'*3001)  # YES -(az)
shuffle(s)
testcases.append(''.join(s))
s = list('ab' + letters[2:-2] * 3000 + 'yz'*3001)  # NO
shuffle(s)
testcases.append(''.join(s))

with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write(f"{t}\n")
    for testcase in testcases:
        in_file.write(f"{testcase}\n")
    for testcase in testcases:
        out_file.write(f"{solve(testcase)}\n")


zipper()


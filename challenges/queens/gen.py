#! /usr/bin/env python3

import sys
from random import randint, choice
from solution import solve

sys.path.append("../")
from utils import *

init()

i = 0
# Samples

n, p, k = 8, 3, 4
pieces = "q b r".split()
positions = [(4, 2), (6, 4), (4, 6)]
obstacles = [(2, 6), (2, 5), (1, 5), (4, 4)]
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}\n{}\n{}\n".format(
                    ' '.join(map(str, (n, p, k))),
                    ' '.join(pieces),
                    '\n'.join(f"{r} {c}" for r, c in positions),
                    '\n'.join(f"{r} {c}" for r, c in obstacles),
                    ))
    out_file.write(f"{solve(n, pieces, positions, set(obstacles)|set(positions), 2)}\n")

i += 1
n, p, k = 2, 2, 0
pieces = "q r".split()
positions = [(1, 1), (2, 2)]
obstacles = []
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}\n{}\n{}".format(
                    ' '.join(map(str, (n, p, k))),
                    ' '.join(pieces),
                    '\n'.join(f"{r} {c}" for r, c in positions),
                    '\n'.join(f"{r} {c}" for r, c in obstacles),
                    ))
    out_file.write(f"{solve(n, pieces, positions, set(obstacles)|set(positions), 2)}\n")

# Random
max_p = 20
piece_types = ('q', 'b', 'r')

for case_set in ((10, 1, 100), (5, 100, 1000), (5, 10000, 100000)):
    print(case_set)
    for _ in range(case_set[0]):
        i += 1
        n = randint(*case_set[1:])
        p = randint(1, max_p if case_set[1] > 1 else min(n**2, max_p))
        k = randint(0, min(n**2 - p, 100000))
        pieces = [choice(piece_types) for _ in range(p)]
        pos_set = set()
        j = 0
        while j < p:
            pos = (randint(1, n), randint(1, n))
            if pos not in pos_set:
                pos_set.add(pos)
                j += 1
        positions = list(pos_set)

        obstacles = []
        j = 0
        while j < k:
            pos = (randint(1, n), randint(1, n))
            if pos not in pos_set:
                obstacles.append(pos)
                j += 1

        with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
            in_file.write("{}\n{}\n{}\n{}".format(
                            ' '.join(map(str, (n, p, k))),
                            ' '.join(pieces),
                            '\n'.join(f"{r} {c}" for r, c in positions),
                            '\n'.join(f"{r} {c}" for r, c in obstacles),
                            ))
            out_file.write(f"{solve(n, pieces, positions, set(obstacles)|pos_set, 2)}\n")

# Targeted

# 1 x 1 board
i += 1
n, p, k = 1, 1, 0
pieces = "q"
positions = [(1, 1)]
obstacles = []
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}\n{}\n{}\n".format(
                    ' '.join(map(str, (n, p, k))),
                    ' '.join(pieces),
                    '\n'.join(f"{r} {c}" for r, c in positions),
                    '\n'.join(f"{r} {c}" for r, c in obstacles),
                    ))
    out_file.write(f"{solve(n, pieces, positions, set(obstacles)|set(positions), 2)}\n")

# Max n and p with no obstacles
i += 1
n, p, k = 100000, 20, 0
pieces = [choice(piece_types) for _ in range(p)]
pos_set = set()
j = 0
while j < p:
    pos = (randint(1, n), randint(1, n))
    if pos not in pos_set:
        pos_set.add(pos)
        j += 1
positions = list(pos_set)
obstacles = []
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}\n{}\n{}\n".format(
                    ' '.join(map(str, (n, p, k))),
                    ' '.join(pieces),
                    '\n'.join(f"{r} {c}" for r, c in positions),
                    '\n'.join(f"{r} {c}" for r, c in obstacles),
                    ))
    out_file.write(f"{solve(n, pieces, positions, set(obstacles)|pos_set, 2)}\n")

# All obstacles on one square
i += 1
n, p, k = 100, 10, 10000
pieces = [choice(piece_types) for _ in range(p)]
pos_set = set()
j = 0
while j < p:
    pos = (randint(1, n), randint(1, n))
    if pos not in pos_set:
        pos_set.add(pos)
        j += 1
positions = list(pos_set)

pos = (randint(1, n), randint(1, n))
while pos in pos_set:
    pos = (randint(1, n), randint(1, n))
obstacles = [pos] 

with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}\n{}\n{}\n".format(
                    ' '.join(map(str, (n, p, k))),
                    ' '.join(pieces),
                    '\n'.join(f"{r} {c}" for r, c in positions),
                    
                    '\n'.join(f"{pos[0]} {pos[1]}" for _ in range(k)),
                    ))
    out_file.write(f"{solve(n, pieces, positions, set(obstacles)|pos_set, 2)}\n")

# Entire board filed
i += 1
n, p = 100, 10
k = n**2 - p
pieces = [choice(piece_types) for _ in range(p)]
pos_set = set()
j = 0
while j < p:
    pos = (randint(1, n), randint(1, n))
    if pos not in pos_set:
        pos_set.add(pos)
        j += 1
positions = list(pos_set)

obstacles = {(x, y) for x in range(1, n+1) for y in range(1, n+1)}
obstacles.difference_update(pos_set)

with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}\n{}\n{}\n".format(
                    ' '.join(map(str, (n, p, k))),
     
                    ' '.join(pieces),
                    '\n'.join(f"{r} {c}" for r, c in positions),
                    '\n'.join(f"{r} {c}" for r, c in obstacles),
                    ))
    out_file.write(f"{solve(n, pieces, positions, obstacles|pos_set, 2)}\n")


# Max n and p, Max p and k
for n, p, k in ((100000, 20, 1000), (10000, 20, 100000)):
    i += 1
    pieces = [choice(piece_types) for _ in range(p)]
    pos_set = set()
    j = 0
    while j < p:
        pos = (randint(1, n), randint(1, n))
        if pos not in pos_set:

            pos_set.add(pos)
            j += 1
    positions = list(pos_set)

    obstacles = []
    j = 0
    while j < k:
        pos = (randint(1, n), randint(1, n))
        if pos not in pos_set:
            obstacles.append(pos)
            j += 1

    with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
            open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
        in_file.write("{}\n{}\n{}\n{}\n".format(
                        ' '.join(map(str, (n, p, k))),
                        ' '.join(pieces),
                        '\n'.join(f"{r} {c}" for r, c in positions),
                        '\n'.join(f"{r} {c}" for r, c in obstacles),
                        ))
        out_file.write(f"{solve(n, pieces, positions, set(obstacles)|pos_set, 2)}\n")


zipper("queens")


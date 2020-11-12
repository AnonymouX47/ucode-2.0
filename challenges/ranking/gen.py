#! /usr/bin/env python3

import sys
from random import choice, randint
from solution import solve

sys.path.append("../")
from utils import *

init()

i = 0
# Samples
n, m = 7, 4
ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}\n{}\n{}".format(n, ' '.join(map(str, ranked)),
                                            m, ' '.join(map(str, player))
                                            ))
    out_file.write('\n'.join(map(str, solve(set(ranked), player))))

i += 1
n, m = 6, 5
ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("{}\n{}\n{}\n{}".format(n, ' '.join(map(str, ranked)),
                                            m, ' '.join(map(str, player))
                                            ))
    out_file.write('\n'.join(map(str, solve(set(ranked), player))))

# Ramdom
for nm_lim in (20, 200, 2000, 20000, 200000):
    for ij_lim in (100, 1000, 10000, 100000, 1000000, 1000000000):
        if nm_lim > ij_lim:
            continue
        i += 1
        print(nm_lim, i)
        n, m = randint(1, nm_lim), randint(1, nm_lim)
        ranked = [randint(0, ij_lim) for _ in range(n)]
        ranked.sort(reverse=True)
        interval = ranked[0] // m
        player = [x + randint(0, 5) for x in range(0, ranked[0]+interval, interval)]
        for _ in range(len(player) - m):
            player.pop(randint(m//2 - 1, m//2 + 1))
        if ranked[0] > player[-1]:
            player[-1] += ranked[0] - player[-1] + randint(1, interval)
        with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
            in_file.write("{}\n{}\n{}\n{}".format(n, ' '.join(map(str, ranked)),
                                                    m, ' '.join(map(str, player))
                                                    ))
            out_file.write('\n'.join(map(str, solve(set(ranked), player))))


zipper()


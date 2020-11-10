import sys
from random import randint
from solution import solve

sys.path.append("../")
from utils import *

init()
solve = timer(solve)

# Sample
with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
        open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
    in_file.write("\n")
    out_file.write(f"{solve()}\n")


worst_case()
zipper("")


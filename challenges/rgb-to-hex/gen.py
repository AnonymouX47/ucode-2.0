from random import randint
from solution import rgb

ranges = ((0, 225), (-1000, -1), (256, 1000))

i = -1
for r in ranges:
    for g in ranges:
        for b in ranges:
            rgb_ranges = (r, g, b)
            t = randint(1, 10)
            i += 1
            with open(f"testcases/input/input{i:02}.txt", 'w') as in_file, \
                    open(f"testcases/output/output{i:02}.txt", 'w') as out_file:
                in_file.write(f"{t}\n")
                for _ in range(t):
                    r_g_b = [randint(*col) for col in rgb_ranges]
                    in_file.write(' '.join(str(col) for col in r_g_b) + '\n')
                    out_file.write(rgb(*r_g_b) + '\n')

from math import ceil

def solve(a, b):
    return int((b ** (1/3) + 0.000001) - ceil(a ** (1/3))) + 1

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solve(*[int(x) for x in input().split()]))

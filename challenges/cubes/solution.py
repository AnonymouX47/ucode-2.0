from math import ceil, floor

def solve(a, b):
    lower = round(a ** (1/3), 8)
    upper = round(b ** (1/3), 8)

    if ceil(lower) == floor(upper):
        return int(lower.is_integer() or upper.is_integer())
    else:
        return floor(upper) - ceil(lower) + 1

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solve(*[int(x) for x in input().split()]))

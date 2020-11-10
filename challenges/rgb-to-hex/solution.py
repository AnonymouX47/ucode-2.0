#! /usr/bin/env python3

def rgb(*args):
    return "#" + ("%02X" * 3) % (*[min(255, max(0, x)) for x in args],)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(rgb(*[int(x) for x in input().split()]))


def total_squares(n: int, pieces: list, positions: list):
    hori_vert = (n-1) * 2
    dia_r_up = lambda r, c: min(n - c, n - r)
    dia_r_dn = lambda r, c: min(n - c, r - 1)
    dia_l_up = lambda r, c: min(c - 1, n - r)
    dia_l_dn = lambda r, c: min(c - 1, r - 1)

    max_squares = {'q': lambda r, c: (hori_vert
                                        + dia_r_up(r, c) + dia_r_dn(r, c)
                                        + dia_l_up(r, c) + dia_l_dn(r, c)),
                    'b': lambda r, c: (dia_r_up(r, c) + dia_r_dn(r, c)
                                        + dia_l_up(r, c) + dia_l_dn(r, c)),
                    'r': lambda r, c: hori_vert
                    }

    return sum([max_squares[piece](*pos) for piece, pos in zip(pieces, positions)])


def solve1(n: int, piece: str, r_p: int, c_p: int, obstacles: set):
    """ Loop over obstacles and check for nearest to each piece in each direction. """

    squares = 0
    # Up
    up = min([r for r,c in obstacles if c==c_q and r>r_q], default=n+1)
    squares += up - r_q - 1
    # Down
    down = max([r for r,c in obstacles if c==c_q and r<r_q], default=0)
    squares += r_q - down - 1
    #Left
    left = max([c for r,c in obstacles if r==r_q and c<c_q], default=0)
    squares += c_q - left - 1
    #Right
    right = min([c for r,c in obstacles if r==r_q and c>c_q], default=n+1)
    squares += right - c_q - 1
    #Left-down
    l_down = max([r for r,c in obstacles if r<r_q and c<c_q and r_q-r==c_q-c],
                    default=0)
    squares += min(r_q-l_down, c_q) - 1
    #right-down
    r_down = max([r for r,c in obstacles if r<r_q and c>c_q and r_q-r==c-c_q],
                    default=0)
    squares += min(r_q-r_down, n+1-c_q) - 1
    #Left-up
    l_up = min([r for r,c in obstacles if r>r_q and c<c_q and r-r_q==c_q-c],
                    default=n+1)
    squares += min(l_up-r_q, c_q) - 1
    #right-up
    r_up = min([r for r,c in obstacles if r>r_q and c>c_q and r-r_q==c-c_q],
                    default=n+1)
    squares += min(r_up-r_q, n+1-c_q) - 1

    return squares


def solve(n: int, pieces: list, positions: list, obstacles, method: int):
    method = (None, solve1, solve2, solve3)[method]

    return max([method(n, piece, *pos, obstacles) for piece, pos in zip(pieces, positions)])


if __name__ == "__main__":
    n, p, k = map(int, input().split())
    pieces = input().split()
    positions = [tuple(input().split()) for _ in range(p)]
    if n == 1:
        print(f"0\n{pieces[0]} {' '.join(positions[0])}\n")
    if total_squares > k:
        method = 1
        obstacles = {tuple(map(int, input().split())) for _ in range(k)}
    elif n <= 20 * 10**3:  # Traverse pieces' paths and check for nearest obstacle using a (1 x N**2) bytearray.
        method = 2
        # Array should use <= ~400MB
        obstacles = bytearray(b'\0') * n**2
        for _ in range(k):
            r, c = map(int, input().split())
            obstacles[n*(r - 1) + c] = 1
        for r, c in positions:
            obstacles[n*(r - 1) + c] = 1
    else:  # Traverse pieces' paths and check for nearest obstacle using membership tests on a set.
        method = 3
        obstacles = {tuple(map(int, input().split())) for _ in range(k)}


    solve(n, pieces, positions, obstacles, method)

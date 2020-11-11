
def queensAttack(n, k, r_q, c_q, obstacles):
    if n == 1: return 0
    if k == 0:
        pass

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



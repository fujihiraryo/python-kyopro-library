def ext_euclid(a, b):
    # 互いに素なa,bに対して、方程式ax+by=1の整数解を1つ求める
    x0, y0, r0 = 1, 0, a
    x1, y1, r1 = 0, 1, b
    while r0:
        x0, x1 = x1 - x0 * (r1 // r0), x0
        y0, y1 = y1 - y0 * (r1 // r0), y0
        r0, r1 = r1 % r0, r0
    return x1, y1, r1


def mod_inv(a, m):
    x, _, r = ext_euclid(a, m)
    if r != 1:
        return -1
    return x % m


def solve(a, b, m):
    # ax=b(mod m)を解く
    _, _, g = ext_euclid(a, m)
    if b % g:
        return -1
    x, y, _ = ext_euclid(a // g, m // g)
    return x * (b // g) % (m // g)


def crt(m, r):
    # 各iでx%m[i]=r[i]となるxを求める
    p = 1
    x = 0
    n = len(m)
    for i in range(n):
        t = (r[i] - x) * mod_inv(p, m[i]) % m[i]
        x += t * p
        p *= m[i]
    return x

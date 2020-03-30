'''
互いに素なa,bに対して、
方程式ax+by=1の整数解を1つ求める
'''


def ext_euclid(a, b):
    x0, y0, r0 = 1, 0, a
    x1, y1, r1 = 0, 1, b
    while r0 != 0:
        x0, y0, r0, x1, y1, r1 = x1 - x0 * (r1 // r0), y1 - y0 * (
            r1 // r0), r1 % r0, x0, y0, r0
    if a * x1 + b * y1 == 1:
        return x1, y1


# テスト
a = 17
b = 33
print(ext_euclid(a, b))
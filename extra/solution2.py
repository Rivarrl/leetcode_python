# -*- coding: utf-8 -*-
# ======================================
# @File    : solution2.py
# @Time    : 2019/10/10 19:10
# @Author  : Rivarrl
# ======================================
import sys


def q1():
    # mihoyo 开发岗1
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    values.sort()
    c = -1
    for i, v in enumerate(values):
        if v != 0:
            c = i
            break
    pre = 'YES+{}'
    if c >= 0:
        q = c
        last = -1
        for v in values[c:][::-1]:
            if last > 0:
                k = last - v - 1
                if k >= 0:
                    c -= k
                else:
                    pre = 'NO+{}'
                    break
            if c < 0:
                pre = 'NO+{}'
                break
            last = v
        print(pre.format(q))
    else:
        # 全是0
        print(pre.format(n))


def q2():
    # 消消乐 没对
    """
    4 4
    0F0E
    0CAC
    GFAD
    AABA
    3 2 3 3
    """

    line1 = sys.stdin.readline().strip()
    m, n = list(map(int, line1.split()))
    chess = []
    for i in range(m):
        # 读取每一行
        line2 = sys.stdin.readline().strip()
        chess.append([e for e in line2])
    line3 = sys.stdin.readline().strip()
    x1, y1, x2, y2 = list(map(int, line3.split()))
    chess[x1][y1], chess[x2][y2] = chess[x2][y2], chess[x1][y1]
    reached = []
    reached.append((x1, y1))
    reached.append((x2, y2))
    def sakuzyo(x, y, c, ij):
        for e in range(x+1, y):
            if ij == 'j':
                chess[c][e] = ''
            else:
                chess[e][c] = ''
    while reached:
        i, j = reached.pop()
        c = chess[i][j]
        if c == '':
            continue
        xi = yi = i
        while xi >= 0 and chess[xi][j] == c:
            xi -= 1
        while yi < n and chess[yi][j] == c:
            yi += 1
        xj = yj = j
        while xj >= 0 and chess[i][xj] == c:
            xj -= 1
        while yj < m and chess[i][yj] == c:
            yj += 1
        # 消除
        if yi - xi - 1 >= 3:
            sakuzyo(xi, yi, j, 'i')
        if yj - xj - 1 >= 3:
            sakuzyo(xj, yj, i, 'j')
        # 下落
        for k in range(n):
            rc = [chess[e][k] for e in range(m)]
            rc.sort()
            for e in range(m):
                chess[e][k] = rc[e]
    print(chess)
    return sum(line.count('') for line in chess)


if __name__ == '__main__':
    a = q2()
    print(a)

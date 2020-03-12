# -*- coding: utf-8 -*-
# ======================================
# @File    : t1.py
# @Time    : 2020/3/12 22:12
# @Author  : Rivarrl
# ======================================
"""
1. 双行道
有一个2*n的网格，有一个人位于(1,1)的位置，即左上角，他希望从左上角走到右下角，即(2,n)的位
置。在每一次，他可以进行三种操作中的一种：
1． 向右走一格，即从(x,y)到(x,y+1);
2． 向上右方走一格，即，如果他在(2,y)的位置可以走到(1,y+1);
3． 向下右方走一格，即，如果他在(1,y)的位置可以走到(2,y+1);
问题当然不会这么简单，在这2*n的格子中，有一部分格子上有障碍物，他不能停在障碍物上，当然也不能
走出网格，请问他有多少种不同的路线可以到达(2,n)。
输入：
5
..X.X
XX...
输出：
2
"""
import sys

def solve():
    n = int(sys.stdin.readline().strip())
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    if line2[n - 1] == 'X': return -1
    res = 1
    for i in range(1, n - 1):
        res *= int(line1[i] == '.') + int(line2[i] == '.')
    return res

if __name__ == '__main__':
    res = solve()
    print(res)
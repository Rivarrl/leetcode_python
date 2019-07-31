# -*- coding:utf-8 -*-
from algorithm_utils import *

# leetcode 困难题

def removeBoxes(boxes):
    """
    546. 移除盒子
    给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
    你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
    当你将所有盒子都去掉之后，求你能获得的最大积分和。
    示例 1：
    输入:
    [1, 3, 2, 2, 2, 3, 4, 3, 1]
    输出:
    23
    解释:
    [1, 3, 2, 2, 2, 3, 4, 3, 1]
    ----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
    ----> [1, 3, 3, 3, 1] (1*1=1 分)
    ----> [1, 1] (3*3=9 分)
    ----> [] (2*2=4 分)
    提示：盒子的总数 n 不会超过 100。
    :param boxes: List[int]
    :return: int
    """
    d = {}
    for x in boxes:
        if not x in d:
            d[x] = 0
        d[x] += 1
    ans = 0
    for i, x in enumerate(boxes):
        if d[boxes[i]] == 1:
            d.pop(boxes[i])
            boxes.pop(i)
            ans += 1
    print(boxes)
    print(d)




if __name__ == '__main__':
    removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])
    pass
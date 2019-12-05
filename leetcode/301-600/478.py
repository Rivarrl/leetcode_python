# -*- coding: utf-8 -*-
# ======================================
# @File    : 478.py
# @Time    : 2019/12/5 11:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import random, math

class Solution:
    """
    [478. 在圆内随机生成点](https://leetcode-cn.com/problems/generate-random-point-in-a-circle/)
    """
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # 随机半径r和弧度theta, theta在[0,2pi]均匀分布, 二维取点, 由面积公式, r^2服从均匀分布, r在[0, radius^2]随机取值后开平方
        r = (random.random() ** 0.5) * self.radius
        theta = random.uniform(0, 2 * math.pi)
        x, y = math.cos(theta) * r, math.sin(theta) * r
        x, y = round(self.x_center + x, 5), round(self.y_center + y, 5)
        return [x, y]

    def randPoint2(self) -> List[float]:
        # 拒绝抽样, 在边长为2*radius的正方形区域随机取样, 计算与圆心的距离如果落入[0,radius]就返回, 否则重复取样
        x = y = self.radius
        while x**2 + y**2 > self.radius**2:
            x, y = (random.random() - 0.5) * 2 * self.radius, (random.random() - 0.5) * 2 * self.radius
        return [self.x_center + x, self.y_center + y]

if __name__ == '__main__':
    # Your Solution object will be instantiated and called as such:
    obj = Solution(10, 5, 7.5)
    param_1 = obj.randPoint2()
    print(param_1)
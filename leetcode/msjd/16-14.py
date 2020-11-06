# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-14.py
# @Time    : 2020/11/5 11:14 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.14. 最佳直线](https://leetcode-cn.com/problems/best-line-lcci/)
    """
    @timeit
    def bestLine(self, points: List[List[int]]) -> List[int]:
        ans = []
        N, max_cnt = len(points), 0
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        for i, p1 in enumerate(points):
            ks = {}
            for fj, p2 in enumerate(points[i+1:]):
                j = fj + i + 1
                if p1[0] == p2[0]:
                    k = '|'
                elif p1[1] == p2[1]:
                    k = '0'
                else:
                    y0 = p2[1] - p1[1]
                    x0 = p2[0] - p1[0]
                    c = gcd(x0, y0)
                    k = '%d/%d'%(y0//c, x0//c)
                ks[k] = ks.get(k, [i]) + [j]
            for vs in ks.values():
                if len(vs) > max_cnt:
                    max_cnt = len(vs)
                    ans = vs[:2]
        return ans

if __name__ == '__main__':
    a = Solution()
    a.bestLine([[0,0],[1,1],[1,0],[2,0]])
    a.bestLine([[-38935,27124],[-39837,19604],[-7086,42194],[-11571,-23257],[115,-23257],[20229,5976],[24653,-18488],[11017,21043],[-9353,16550],[-47076,15237],[-36686,42194],[-17704,1104],[31067,7368],[-20882,42194],[-19107,-10597],[-14898,24506],[-20801,42194],[-52268,40727],[-14042,42194],[-23254,42194],[-30837,-53882],[1402,801],[-33961,-984],[-6411,42194],[-12210,22901],[-8213,-19441],[-26939,20810],[30656,-23257],[-27195,21649],[-33780,2717],[23617,27018],[12266,3608]])
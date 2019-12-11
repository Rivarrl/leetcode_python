# -*- coding: utf-8 -*-
# ======================================
# @File    : 282.py
# @Time    : 2019/12/11 11:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [282. 给表达式添加运算符](https://leetcode-cn.com/problems/expression-add-operators/)
    """
    @timeit
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        思路: 回溯, 不要到递归结束再去做运算, 那样会产生很多重复运算, 走一步算一步的, 遇到乘法把前面+/-的复原再加乘过的结果
        """
        n = len(num)
        if n == 0: return []
        res = []
        def dfs(num, exp, prev, ans):
            if not num and ans == target:
                res.append(exp)
            else:
                for i in range(1, len(num)+1):
                    if i > 1 and num[0] == '0': continue
                    left, right = num[:i], num[i:]
                    cur = int(left)
                    if not exp: dfs(right, left, cur, cur)
                    else:
                        dfs(right, exp + '+' + left, cur, ans + cur)
                        dfs(right, exp + '-' + left, -cur, ans - cur)
                        dfs(right, exp + '*' + left, prev*cur, ans + prev * (cur-1))

        dfs(num, '', 0, 0)
        return res

if __name__ == '__main__':
    a = Solution()
    a.addOperators('123', 6)
    a.addOperators('232', 8)
    a.addOperators('105', 5)
    a.addOperators('00', 0)
    a.addOperators('3456237490', 9191)
    a.addOperators('1001', 101)
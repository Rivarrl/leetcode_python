# -*- coding: utf-8 -*-
# ======================================
# @File    : 1773.py
# @Time    : 2021/3/3 23:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [1773. 统计匹配检索规则的物品数量](https://leetcode-cn.com/problems/count-items-matching-a-rule/)
    """
    @timeit
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for t, c, n in items:
            if (ruleKey == 'type' and t == ruleValue) or (ruleKey == 'color' and c == ruleValue) or (ruleKey == 'name' and n == ruleValue):
                res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver")
    a.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone")
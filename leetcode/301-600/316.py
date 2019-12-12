# -*- coding: utf-8 -*-
# ======================================
# @File    : 316.py
# @Time    : 2019/12/12 11:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [316. 去除重复字母](https://leetcode-cn.com/problems/remove-duplicate-letters/)
    """
    @timeit
    def removeDuplicateLetters(self, s: str) -> str:
        """
        思路: 递归去找, 如果按当前字典序最小的位置选择字符, 后面还有一整套的s元素, 那么说明这个字符一定是最终答案中的字符
        """
        def dfs(s):
            for c in sorted(set(s)):
                tmp = s[s.index(c):]
                if len(set(tmp)) == len(set(s)):
                    return c + dfs(tmp.replace(c, ''))
            return ''
        return dfs(s)

    @timeit
    def removeDuplicateLetters2(self, s: str) -> str:
        """
        思路: 栈, 每次找到更小的时候, 如果后面还有栈顶元素就弹栈
        """
        stk = ['A']
        for i, c in enumerate(s):
            while not c in stk and stk[-1] > c and s.find(stk[-1], i) != -1:
                stk.pop()
            if not c in stk: stk.append(c)
        return ''.join(stk[1:])

if __name__ == '__main__':
    a = Solution()
    a.removeDuplicateLetters2("bcabc")
    a.removeDuplicateLetters2("cbacdcbc")
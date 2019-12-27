# -*- coding: utf-8 -*-
# ======================================
# @File    : 388.py
# @Time    : 2019/12/16 13:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [388. 文件的最长绝对路径](https://leetcode-cn.com/problems/longest-absolute-file-path/)
    """
    @timeit
    def lengthLongestPath(self, input: str) -> int:
        words = input.split('\n')
        stk = []
        res = 0
        cur = 0
        for i, word in enumerate(words):
            level = word.count('\t')
            while stk and stk[-1][1] >= level:
                cur -= stk.pop()[0]
            size = len(word.lstrip('\t'))
            stk.append([size, level])
            cur += size
            if word.find('.') >= 0 and cur + level > res:
                res = cur + level
        return res

if __name__ == '__main__':
    a = Solution()
    a.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    a.lengthLongestPath("a\n\taa\n\t\taaa\n\t\t\tfile1234567890123.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png")
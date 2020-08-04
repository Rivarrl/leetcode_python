# -*- coding: utf-8 -*-
# ======================================
# @File    : 1410.py
# @Time    : 2020/7/24 23:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
class Solution:
    """
    [1410. HTML 实体解析器](https://leetcode-cn.com/problems/html-entity-parser/)
    """
    @timeit
    def entityParser(self, text: str) -> str:
        d = {
            "&quot;":"\"",
            "&apos;":"'",
            "&amp;":"&",
            "&gt;":">",
            "&lt;":"<",
            "&frasl;":"/"
        }
        res = ''
        tmp = -1
        flag = 0
        for i in range(len(text)):
            if text[i] == '&':
                tmp = i
                flag = 1
            elif flag == 0:
                res += text[i]
            elif text[i] == ';':
                if text[tmp:i+1] in d:
                    res += d[text[tmp:i+1]]
                else:
                    res += text[tmp:i+1]
                flag = 0
        return res


if __name__ == '__main__':
    a = Solution()
    a.entityParser(text = "&amp; is an HTML entity but &ambassador; is not.")
    a.entityParser(text = "and I quote: &quot;...&quot;")
    a.entityParser(text = "Stay home! Practice on Leetcode :)")
    a.entityParser(text = "x &gt; y &amp;&amp; x &lt; y is always false")
    a.entityParser(text = "leetcode.com&frasl;problemset&frasl;all")
    a.entityParser("&amp;amp;")
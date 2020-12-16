# -*- coding: utf-8 -*-
# ======================================
# @File    : 591.py
# @Time    : 2020/12/16 10:16 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [591. 标签验证器](https://leetcode-cn.com/problems/tag-validator/)
    """
    @timeit
    def isValid(self, code: str) -> bool:
        n = len(code)
        i = 0
        stk = []
        while i < n:
            if code[i] == '<':
                # CDATA
                if i + 1 < n and code[i+1] == '!':
                    # 外面没有标签
                    if not stk: return False
                    # 不满足 <![CDATA[]]>
                    if i + 12 >= n: return False
                    if code[i:i+9] != '<![CDATA[': return False
                    i += 9
                    while i + 2 < n and code[i:i+3] != ']]>':
                        i += 1
                    if i + 2 == n: return False
                    i += 2
                else:
                    # </??>
                    if i + 1 < n and code[i+1] == '/':
                        i += 1
                        sym = 1
                    else:
                        sym = 0
                    i += 1
                    # <??>
                    j = i
                    while i < n and code[i] != '>':
                        if not ord('A') <= ord(code[i]) <= ord('Z'): return False
                        i += 1
                    # <... or <> or <?*10>
                    if i == n or i == j or i - j > 9: return False
                    t = code[j:i]
                    if sym == 0:
                        stk.append(t)
                    else:
                        if not stk or stk[-1] != t:
                            return False
                        stk.pop()
            i += 1
            if not stk and i < n: return False
        return len(stk) == 0


    @timeit
    def isValid2(self, code: str) -> bool:
        # 欢乐正则人
        import re
        code, n = re.subn("^<(?P<div>[A-Z]{1,9})>(.*?)</(?P=div)>$", lambda x: x.group(2), code)
        if n == 0: return False
        code = re.sub("<!\[CDATA\[.*?\]\]>", "", code)
        if '<!' in code: return False
        while n:
            code, n = re.subn("<(?P<div>[A-Z]{1,9})>(.*?)</(?P=div)>", lambda x: x.group(2), code)
        return '<' not in code

if __name__ == '__main__':
    a = Solution()
    # a.isValid2("<DIV>This is the first line <![CDATA[<div>]]></DIV>")
    # a.isValid2("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")
    # a.isValid2("<A>  <B> </A>   </B>")
    # a.isValid2("<DIV>  div tag is not closed  <DIV>")
    # a.isValid2("<DIV>  unmatched <  </DIV>")
    # a.isValid2("<DIV> closed tags with invalid tag name  <b>123</b> </DIV>")
    # a.isValid2("<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>")
    # a.isValid2("<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>")
    a.isValid2("<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>")
    # a.isValid2("<TRUe><![CDATA[123123]]]]><![CDATA[>123123]]></TRUe>")
    # a.isValid2("<A></A><B></B>")
    # a.isValid2("<A><![CDATA[</A>]]123></A>")
    # a.isValid2("<AAAAAAAAAA></AAAAAAAAAA>")
    # a.isValid2("<A><B></B></A>")
    # a.isValid2("<DIV>>>>>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")
    # a.isValid2("<A></A>>")
    # a.isValid2("<A><A>456</A>  <A> 123  !!  <![CDATA[]]>  123 </A>   <A>123</A></A>")
    # a.isValid2("<![CDATA[ABC]]><TAG>sometext</TAG>")
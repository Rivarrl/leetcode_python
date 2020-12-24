# -*- coding: utf-8 -*-
# ======================================
# @File    : 722.py
# @Time    : 2020/12/24 1:34 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [722. 删除注释](https://leetcode-cn.com/problems/remove-comments/)
    """
    @timeit
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        s = '\n'.join(source)
        # row = 0:'/', 1:'*', 2:'\n', 3:'other'
        fsm = [[1, 2, 2, 3, 0],
               [0, 3, 2, 4, 4],
               [0, 0, 0, 3, 3],
               [0, 0, 2, 3, 3]]
        # 状态变化时做的动作，1: append, 0: pass, -1: pop, -2：不可能发生的变化
        action = [[1, 1, 1, 1, 1],
                  [1, -2, -1, -1, -2],
                  [1, -2, 0, -2, -2],
                  [-2, -2, -2, 0, 0],
                  [0, -2, -2, 0, 0]]
        def next_state(c, st):
            if c == '/':
                return fsm[0][st]
            elif c == '*':
                return fsm[1][st]
            elif c == '\n':
                return fsm[2][st]
            else:
                return fsm[3][st]
        st = 0
        for c in s:
            nst = next_state(c, st)
            if action[st][nst] == -1:
                res.pop()
            elif action[st][nst] == 1:
                res.append(c)
            st = nst
        return [e for e in ''.join(res).split('\n') if e]

if __name__ == '__main__':
    a = Solution()
    a.removeComments(source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
    a.removeComments(source = ["a/*comment", "line", "more_comment*/b"])
    a.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"])
    a.removeComments(["main() {", "/* here is commments", "  // still comments */", "   double s = 33;", "   cout << s;", "}"])
    a.removeComments(["a/*/b//*c","blank","d//*e/*/f"])
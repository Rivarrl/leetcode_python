# -*- coding: utf-8 -*-
# ======================================
# @File    : 609.py
# @Time    : 2020/12/16 9:58 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [609. 在系统中查找重复文件](https://leetcode-cn.com/problems/find-duplicate-file-in-system/)
    """
    @timeit
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for path in paths:
            arr = path.split(' ')
            p = arr[0]
            for x in arr[1:]:
                f, c = x[:-1].split('(')
                d[c] = d.get(c, list()) + ['{}/{}'.format(p, f)]
        return list([e for e in d.values() if len(e) > 1])


if __name__ == '__main__':
    a = Solution()
    a.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])

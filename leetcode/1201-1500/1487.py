# -*- coding: utf-8 -*-
# ======================================
# @File    : 1487.py
# @Time    : 2020/6/28 1:00 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1487. 保证文件名唯一](https://leetcode-cn.com/problems/making-file-names-unique/)
    """
    @timeit
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = {}
        res = []
        for x in names:
            cur = d.get(x, 0)
            if cur == 0:
                res.append(x)
            else:
                i = cur
                y = '{}({})'.format(x, i)
                while y in d:
                    i += 1
                    y = '{}({})'.format(x, i)
                d[y] = 1
                res.append(y)
            d[x] = cur + 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.getFolderNames(names = ["pes","fifa","gta","pes(2019)"])
    a.getFolderNames(names = ["gta","gta(1)","gta","avalon"])
    a.getFolderNames(names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"])
    a.getFolderNames(names = ["wano","wano","wano","wano"])
    a.getFolderNames(names = ["kaido","kaido(1)","kaido","kaido(1)"])
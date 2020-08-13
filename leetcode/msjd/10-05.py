# -*- coding: utf-8 -*-
# ======================================
# @File    : 10-05.py
# @Time    : 2020/8/14 0:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 10.05. 稀疏数组搜索](https://leetcode-cn.com/problems/sparse-array-search-lcci/)
    """
    @timeit
    def findString(self, words: List[str], s: str) -> int:
        n = len(words)
        def gt(s, t):
            n1, n2 = len(s), len(t)
            for i in range(min(n1, n2)):
                if s[i] != t[i]:
                    return ord(s[i]) > ord(t[i])
            return n1 > n2
        lo, hi = 0, n
        while lo < hi:
            while lo < hi and words[lo] == '':
                lo += 1
            while lo < hi and words[hi-1] == '':
                hi -= 1
            mi = lo + hi >> 1
            while words[mi] == '':
                mi -= 1
            if s == words[mi]:
                return mi
            elif gt(s, words[mi]):
                lo = mi + 1
            else:
                hi = mi
        return -1

if __name__ == '__main__':
    a = Solution()
    # a.findString(words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta")
    # a.findString(words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball")
    # a.findString(["DirNnILhARNS hOYIFB", "SM ", "YSPBaovrZBS", "evMMBOf", "mCrS", "oRJfjw gwuo", "xOpSEXvfI"], "mCrS")
    a.findString(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""],"ta")
    a.findString(["", "", "", "", "", " dQWlBwMkQGCAH", "", "", "", "", "", "", "", "", " kbmYemYUbb", "", "", "", "", "", "AhdDHirVKcLkr ", "", "", "", "", "", "", "", "", "", "", "", "BNAbUAatDzPXTHQfEhiH", "", "", "", "", "", "BRrrNNUbmm", "", "", "BrluxJYeZ", "", "", "", "", "", "", "", "", "", "", "C", "", "", "", "COZgRwNRaTVH", "", "", "", "", "", "", "", "", "", "COy", "", "", "", "", "", "CZiiiXfgR", "", "", "", "", "", "", "", "", "CvsytGxtr", "", "", "", "", "DYgNOJzvt dKo", "", "", "", "", "", "", "", "", "ETxOvZADWeGZymn", "", "", "", "", "Enw", "", "", "", "", "ErObvXdjyJ", "", "", "", "", "", "", "", "Fxt", "", "", "", "", "", "Hcg", "", "IFCmcsMQZVDw", "", "", "", "", "", "IxwAsjDo", "", "", "", "", "JJRmOfMVv", "", "", "", "", "", "", "", "", "", "KbmELArhbtQloxzJkOZB", "", "", "KmrXslnWHv bviiXljAK", "", "", "", "", "", "KoQgClvxqrOEIM nCY", "", "", "", "", "", "LBZAnpDJskac", "", "LKSy", "", "", "", "", "", "LMCUFc ynZCbTqJRDOIH", "", "", "", "", "", "", "", "", "", "LZui eEOVxOo", "", "", "", "", "", "", "LmeGZUSZgqJ", "", "", "", "MMsARKwsJ", "", "", "My", "", "", "", "NGcuzKOVRNyqDFuE", "", "", "NHEReECTTxUCeElZquZe", "", "", "", "", "OKoDrnWrGZyTYUDS", "", "", "", "", "", "", "", "", "", "OitAuWpxzogGOVGbVqRc", "", "", "", "", "", "", "", "", "OvSVSZYgfaTD", "", "", "PW", "", "", "", "", "", "", "", "", "", "Pf", "", "PmqWrQsrrFVpQe", "", "", "", "", "", "", "", "", "", "QSZxNOguO", "", "", "", "", "QxhpjdwPNUOTj", "", "", "", "", "", "", "", "", "", "R", "", "", "", "", "", "RZZnlbAHKZJH", "", "", "", "", "", "", "RcrNcLvsvCdYCe", "", "", "", "", "", "RunaVcyf", "", "", "SkCZwclZ", "TNawyWMprE", "", "", "", "", "", "", "", "", "TUKi", "TeBcKqVdjVIJtzRy", "", "", "TmGbS GYWH", "", "", "", "", "", "UgjPSTLdQAesaBYVV", "", "", "UnpPgKLLgnHsDRw", "VDHEYbbmcSibGkoOY", "", "", "VFhbWJAydDCFyZvbFA", "", "", "", "", "", "", "", "", "", "", "", "VWQZxHx YvKZgxkScVR", "", "", "", "", "", "WJqaQdZZXBrXXtIWGq", "", "", "WiAdRTHgdJNLKZPrV", "", "", "", "", "", "", "", "", "X", "", "", "", "", "", "", "XgbKyxpd", "", "", "", "XjYPV", "", "", "", "", "", "", "", "YNY UFJJNRMHtA", "", "", "", "", "", "", "", "YeNY", "", "", "", "", "", "", "", "", "", "ZKcuWQvdKD", "", "", "", "ZjjfTUB", "", "", "", "", "", "", "ZxhS", "", "", "", "", "", "", "aNRzbCptSLqKcwHn", "", "", "", "", "", "", "aWTfJvpFLsNzL", "", "", "", "", "", "", "", "", "", "aquRNbNXxsRQwBHVeIWa", "", "", "", "", "", "bsy", "", "", "", "", "", "", "c cxJUciWsLmXZSCIG", "", "", "", "", "", "", "dHGYGGa", "", "", "eBnLl", "", "ffesVvulHsm", "", "", "", "", "", "", "", "", "", "", "", "ggXhLRpAHZYPh", "", "", "", "", "", "", "", "", "", "", "", "gksuHImKFIzbHmQBzksg", "grWcl", "", "", "", "", "", "", "hLwNisMg", "", "", "", "", "", "", "", "", "", "", "htZGqEaqFSsHlDQX", "", "", "", "", "", "", "", "", "", "jGppHHwT", "jd", "", "", "", "", "", "", "", "kWof", "", "", "", "", "", "", "", "kvPEgk", "lDBdeQZRgQNlDIP", "", "", "", "", "", "", "", "", "", "lIceBio", "", "", "", "", "", "", "", "", "", "", "", "mIIIss", "", "", "", "", "", "", "", "", "", "mJKai", "", "", "", "", "muIekSC", "", "nMJipECkkgnEcMmyfob", "", "", "", "", "", "", "", "nXivxaBbI", "q", "", "", "", "", "", "", "", "", "", "qAmqnvNBHnB", "", "", "", "", "", "", "", "", "", "qPOf tD", "", "", "", "", "", "", "", "", "", "qilsrkiifEeOj", "", "", "", "", "", "", "", "", "", "rPfjvzoHWzecujWUoRX", "", "", "", "", "rYf", "", "", "", "", "", "", "", "", "", "", "", "sGUgT PfifYJYdkd", "", "", "", "", "", "", "", "", "", "sf LOmMcRojVEc", "", "tvJQ", "", "", "", "", "uabKCYiiKmmpUns", "", "", "", "", "", "", "", "", "", "", "", "udz", "", "uqSPk OkChjuD", "", "", "", "", "", "", "y", "", "", "", "", "", "yHQWPlWSNwtb", "", "", "", "", "", "", "", "", "", "", "yWfXCUsa", "", "", "", "", "", "", "zEZXmgrvQoOTwOKoEIEd", "", "", "zZEMDDvzsOgTmzc", "", "", "", "", "", "", "", "", "", "", "", "zk", "", "", "", "", "", "", "", "", "znWcoGeFJicW nPjHUGm"]
,"kKfytHTqoIrKNCQjzJIF")
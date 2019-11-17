# -*- coding: utf-8 -*-
# ======================================
# @File    : 5110.py
# @Time    : 2019/11/16 22:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    5110. 近义词句子
    给你一个近义词表 synonyms 和一个句子 text ， synonyms 表中是一些近义词对 ，你可以将句子 text 中每个单词用它的近义词来替换。
    请你找出所有用近义词替换后的句子，按 字典序排序 后返回。
    示例 1：
    输入：
    synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
    text = "I am happy today but was sad yesterday"
    输出：
    ["I am cheerful today but was sad yesterday",
    "I am cheerful today but was sorrow yesterday",
    "I am happy today but was sad yesterday",
    "I am happy today but was sorrow yesterday",
    "I am joy today but was sad yesterday",
    "I am joy today but was sorrow yesterday"]
    提示：
    0 <= synonyms.length <= 10
    synonyms[i].length == 2
    synonyms[0] != synonyms[1]
    所有单词仅包含英文字母，且长度最多为 10 。
    text 最多包含 10 个单词，且单词间用单个空格分隔开。
    """
    @timeit
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        from collections import defaultdict
        n = len(synonyms)
        d = {}
        rd = defaultdict(set)
        tot = 0
        for i in range(n):
            x, y = synonyms[i]
            c = tot
            if x in d:
                c = d[x]
            if y in d:
                c = d[y]
            d[x] = d[y] = c
            rd[c].add(x)
            rd[c].add(y)
            tot += 1
        words = text.split(' ')
        txn = len(words)
        res = []
        def dfs(i, cur):
            nonlocal res
            if i == txn:
                res.append(' '.join(cur))
                return
            if words[i] in d:
                for x in rd[d[words[i]]]:
                    dfs(i + 1, cur + [x])
            else:
                dfs(i+1, cur + [words[i]])
        dfs(0, [])
        return sorted(res)


if __name__ == '__main__':
    a = Solution()
    a.generateSentences(synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
                        text = "I am happy today but was sad yesterday")
    a.generateSentences([["a","b"],["c","d"],["e","f"]], "a c e")



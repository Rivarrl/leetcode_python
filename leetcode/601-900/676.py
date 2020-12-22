# -*- coding: utf-8 -*-
# ======================================
# @File    : 676.py
# @Time    : 2020/12/22 4:52 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from collections import defaultdict

class MagicDictionary:
    """
    [676. 实现一个魔法字典](https://leetcode-cn.com/problems/implement-magic-dictionary/)
    """
    def __init__(self):
        self.magic_dict = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                self.magic_dict[word[:i] + '*' + word[i+1:]].add(word[i])

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            s = searchWord[:i] + '*' + searchWord[i + 1:]
            if s in self.magic_dict and (len(self.magic_dict[s]) > 1 or searchWord[i] not in self.magic_dict[s]):
                return True
        return False

if __name__ == '__main__':
    a = MagicDictionary()
    a.buildDict(["hello", "hallo", "leetcode"])
    print(a.search("hello"))
    print(a.search("hallo"))
    print(a.search("hell"))
    print(a.search("leetcoded"))

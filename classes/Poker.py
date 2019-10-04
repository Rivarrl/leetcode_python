# -*- coding: utf-8 -*-
# ======================================
# @File    : Poker.py
# @Time    : 2019/10/5 0:41
# @Author  : Rivarrl
# ======================================

import random


class Poker:
    def __init__(self, shuffle=False, transform=True):
        self.trans = {
            "#": "红桃",
            "$": "黑桃",
            "^": "方片",
            "*": "梅花",
            "R": "大王",
            "B": "小王"
        }
        self.pk = ["A"]
        self.pk.extend(str(i) for i in range(1, 11))
        self.pk.extend(["J", "Q", "K"])
        self.poker = []
        self.new(self.poker)
        if shuffle:
            self.shuffle()
        if transform:
            self.transfrom()


    def new(self, poker):
        for k in self.trans.keys():
            if k in {"B", "R"}:
                continue
            for p in self.pk:
                poker.append(k + p)
        poker.append("B")
        poker.append("R")

    def transfrom(self):
        for i, e in enumerate(self.poker):
            self.poker[i] = self.trans[e[0]] + e[1:]

    def shuffle(self):
        cur = [e for e in self.poker]
        for i in range(52, 0, -1):
            j = random.randint(0, i)
            self.poker[i] = cur.pop(j)


if __name__ == '__main__':
    p = Poker()
    for e in p.poker:
        print(e)
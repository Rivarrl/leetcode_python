# -*- coding: utf-8 -*-
# ======================================
# @File    : 5390.py
# @Time    : 2020/4/19 11:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5390. 数青蛙]()
    """
    @timeit
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        res = c = r = o = a = k = 0
        for e in croakOfFrogs:
            if e == 'c':
                c += 1
            elif e == 'r':
                r += 1
            elif e == 'o':
                o += 1
            elif e == 'a':
                a += 1
            elif e == 'k':
                k += 1
            else: return -1
            if c < r or r < o or o < a or a < k: return -1
            res = max(res, c)
            if k == 1:
                c -= 1
                r -= 1
                o -= 1
                a -= 1
                k -= 1
        if c != 0: return -1
        return res

if __name__ == '__main__':
    a = Solution()
    a.minNumberOfFrogs("croakcroak")
    a.minNumberOfFrogs("crcoakroak")
    # a.minNumberOfFrogs("croakcrook")
    a.minNumberOfFrogs("croakcroa")
    a.minNumberOfFrogs("crocakcroraoakk")
    a.minNumberOfFrogs("cccroarorakoakkcroak")
    a.minNumberOfFrogs("ccccccccccrrccccccrcccccccccccrcccccccccrcccccccccccrcccccrcccrrcccccccccccccrocrrcccccccccrccrocccccrccccrrcccccccrrrcrrcrccrcoccroccrccccccccorocrocccrrrrcrccrcrcrcrccrcroccccrccccroorcacrkcccrrroacccrrrraocccrrcrrccorooccrocacckcrcrrrrrrkrrccrcoacrcorcrooccacorcrccccoocroacroraoaarcoorrcrcccccocrrcoccarrorccccrcraoocrrrcoaoroccooccororrrccrcrocrrcorooocorarccoccocrrrocaccrooaaarrcrarooaarrarrororrcrcckracaccorarorocacrrarorrraoacrcokcarcoccoorcrrkaocorcrcrcrooorrcrroorkkaaarkraroraraarooccrkcrcraocooaoocraoorrrccoaraocoorrcokrararrkaakaooroorcororcaorckrrooooakcarokokcoarcccroaakkrrororacrkraooacrkaraoacaraorrorrakaokrokraccaockrookrokoororoooorroaoaokccraoraraokakrookkroakkaookkooraaocakrkokoraoarrakakkakaroaaocakkarkoocokokkrcorkkoorrkraoorkokkarkakokkkracocoaaaaakaraaooraokarrakkorokkoakokakakkcracarcaoaaoaoorcaakkraooaoakkrrroaoaoaarkkarkarkrooaookkroaaarkooakarakkooaokkoorkroaaaokoarkorraoraorcokokaakkaakrkaaokaaaroarkokokkokkkoakaaookkcakkrakooaooroaaaaooaooorkakrkkakkkkaokkooaakorkaroaorkkokaakaaaaaocrrkakrooaaroroakrakrkrakaoaaakokkaaoakrkkoakocaookkakooorkakoaaaaakkokakkorakaaaaoaarkokorkakokakckckookkraooaakokrrakkrkookkaaoakaaaokkaokkaaoakarkakaakkakorkaakkakkkakaaoaakkkaoaokkkakkkoaroookakaokaakkkkkkakoaooakcokkkrrokkkkaoakckakokkocaokaakakaaakakaakakkkkrakoaokkaakkkkkokkkkkkkkrkakkokkroaakkakaoakkoakkkkkkakakakkkaakkkkakkkrkoak")
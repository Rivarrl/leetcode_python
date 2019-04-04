# -*- coding:utf-8 -*-

## 贪心算法

class Activity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start if self.end == other.end else self.end < other.end


def activity_selector(s, f):
    """
    活动选择问题，教室同一时刻只能有一个活动占用，s为活动开始时间列表，f为结束时间列表，最多可以排多少活动
    利用贪心算法，按结束时间顺序排序后，选择活动执行时间最短的。
    :param s:
    :param f:
    :return:
    """
    list_act = []
    for x, y in zip(s, f):
        list_act.append(Activity(x, y))
    list_act.sort()
    i = 0
    total = 1
    for j in range(1, list_act.__len__()):
        if list_act[j].start >= list_act[i].end:
            i = j
            total += 1
    return total

def money_resolve(money, s, n):
    """
    钱币付款问题，有不同面值s的纸币分别数张n，用这些钱支付money元，至少要用多少张纸币？
    :param money:
    :param s:
    :param n:
    :return:
    """
    l = s.__len__()
    # 倒序排序面值s和数量n列表
    for i in range(l):
        for j in range(i + 1, l):
            if s[j] > s[i]:
                s[j], s[i] = s[i], s[j]
                n[j], n[i] = n[i], n[j]
    # 计算纸币张数
    total = 0
    for i in range(l):
        p = money // s[i]
        if p > 0 and n[i] >= p:
            money -= s[i] * p
            n[i] -= p
            total += p
    if money != 0:
        total += 1
    return total


if __name__ == '__main__':
    s = [1, 5, 3, 5, 3, 0, 6, 8, 8, 2, 12]
    f = [4, 7, 8, 9, 5, 6, 10, 11, 12, 13, 14]
    ans1 = activity_selector(s, f)
    # print("活动选择答案：", ans1)

    s = [1,2,5,10,20,50,100]
    n = [3,0,2,1,0,3,5]
    ans2 = money_resolve(154, s, n)
    print("纸币找零答案：", ans2)
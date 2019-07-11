# -*- coding:utf-8 -*-
from leetcode import algorithm_utils as alg


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
    注：总钱数一定>=money，付款要付够
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


def boat(sp):
    """
    POJ1700
    小船过河问题
    有一艘船，能乘2人，船的运行速度为2人中较慢一人的速度，过去后还需一个人把船划回来，问把n个人运到对岸，最少需要多久。
    思路：
    将所有人过河所需的时间按照升序排序，将当前单独过河所需时间最多的两人先送到对岸，有两种方式：
    1.最快的和次快的过河，然后最快的将船划回来；次慢的和最慢的过河，然后次快的将船划回来，所需时间为：t[0]+2*t[1]+t[n-1]；
    2.最快的和最慢的过河，然后最快的将船划回来，最快的和次慢的过河，然后最快的将船划回来，所需时间为：2*t[0]+t[n-2]+t[n-1]。
    除上述方法外，其他方法用时更多。
    且每次运送耗时最长的两个人不影响其他人，故问题具有贪心子结构的性质。
    :param sp: List[int]
    :return: int
    """
    l = len(sp)
    alg.quick_sort(sp, 0, l - 1)
    ans = 0
    while l > 3:
        ans = ans + min(sp[1] + sp[0] + sp[l-1] + sp[1], sp[l-1] + sp[0] + sp[l-2] + sp[0])
        l -= 2
    if l == 3:
        ans += sp[0] + sp[1] + sp[2]
    elif l == 2:
        ans += sp[1]
    else:
        ans += sp[0]
    return ans




if __name__ == '__main__':
    # s = [1, 5, 3, 5, 3, 0, 6, 8, 8, 2, 12]
    # f = [4, 7, 8, 9, 5, 6, 10, 11, 12, 13, 14]
    # ans1 = activity_selector(s, f)
    # print("活动选择答案：", ans1)

    # s = [1,2,5,10,20,50,100]
    # n = [3,0,2,1,0,3,5]
    # ans2 = money_resolve(154, s, n)
    # print("纸币找零答案：", ans2)

    sp = [4, 3, 1, 5, 6]
    ans3 = boat(sp)
    print("小船过河答案：", ans3)
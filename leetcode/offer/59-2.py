# 面试题59 - II. 队列的最大值

from algorithm_utils import *

class MaxQueue:

    def __init__(self):
        self.q = []
        self.tmp = []

    def max_value(self) -> int:
        return self.tmp[0] if self.q else -1

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.tmp and self.tmp[-1] < value:
            self.tmp.pop()
        self.tmp.append(value)

    def pop_front(self) -> int:
        if not self.q: return -1
        res = self.q.pop(0)
        if self.tmp[0] == res:
            self.tmp.pop(0)
        return res


if __name__ == '__main__':
    mq = MaxQueue()
    mq.push_back(1)
    mq.push_back(2)
    mq.max_value()
    mq.pop_front()
    mq.max_value()
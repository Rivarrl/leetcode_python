from algorithm_utils import *

@timeit
def init_array(n, m):
    x = [[0x3fffff] * n for _ in range(m)]


if __name__ == '__main__':
    init_array(10, 600000)
    init_array(600000, 10)
    pass
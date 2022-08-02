# -*- coding: utf-8 -*-
"""
@author: WangJianWei
@time: 2022/8/2 21:51
"""
nums = [2, 7, 11, 15]
target = 26


def solution():
    data = dict()
    for i, n in enumerate(nums):
        o = data.get(target - n)
        if o is not None:
            return i, o

        data[n] = i


if __name__ == '__main__':
    print(solution())

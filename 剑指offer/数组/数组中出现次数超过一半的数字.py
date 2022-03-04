"""
给一个长度为 n 的数组，数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。

数据范围：n≤50000，数组中元素的值 0≤val≤10000
要求：空间复杂度：O(1)，时间复杂度 O(n)
输入描述：
保证数组输入非空，且保证有解
"""


class Solution:
    """
    解题思路：使用字典的key来保存数组中的值，使用字典中的val来保存对应key出现的次数
    """
    def MoreThanHalfNum(self, val: list[int]) -> int:
        dic = {}
        size = len(val)
        for i in range(size):
            if val[i] not in dic.keys():
                dic[val[i]] = 1
            else:
                dic[val[i]] += 1

        for k, v in dic.items():
            if dic[k] > (size//2):
                return k


if __name__ == '__main__':
    a = Solution()
    ret = [3, 3, 3, 3, 2, 2, 2]
    result = a.MoreThanHalfNum(ret)
    print(result)
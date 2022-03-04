"""
输入一个长度为 n 整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。

数据范围：0≤n≤5000，数组中每个数的值0≤val≤10000
要求：时间复杂度 O(n)，空间复杂度 O(n)
进阶：时间复杂度 O(n^2)，空间复杂度 O(1)
"""


class Solution:
    def swaparr(self, array: list[int]) -> list:
        ret = []
        res = []
        for i in array:
            if i % 2 == 0:
                ret.append(i)
            if i % 2 != 0:
                res.append(i)
        res.extend(ret)
        return res


if __name__ == '__main__':
    a = Solution()
    numbers = [1, 2, 3, 4]
    result = a.swaparr(numbers)
    print(result)
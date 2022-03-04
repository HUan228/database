"""
JZ10
大家都知道斐波那契数列，现在要求输入一个正整数 n ，请你输出斐波那契数列的第 n 项。
数据范围：1≤n≤40
要求：空间复杂度O(1)，时间复杂度O(n)，本题也有时间复杂度 O(logn)的解法

输入描述：
一个正整数n
返回值描述：
输出一个正整数。
"""


class Solution:
    """
    解题思路：斐波拉契数列：1 1 2 3 5 8 13 21.。。
    0，1都为1， 当从第2个数开始时，值变为了前两个数相加的和(下标从0开始)
    """
    def fibo(self, val: int) -> int:
        if val < 0:
            return -1
        if val < 2:
            return 1
        a, b = 0, 1
        for i in range(val):
            a, b = b, a+b
        return b


if __name__ == '__main__':
    res = Solution()
    print(res.fibo(5))
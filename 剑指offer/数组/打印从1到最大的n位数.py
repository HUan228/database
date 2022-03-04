"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
1. 用返回一个整数列表来代替打印
2. n 为正整数，0 < n <= 5
"""


class Solution:
    """
    解题思路：因为是打印从1到与传入值相同位数的最大值
            通过求幂的方法可以求得比该数的最大值大1的数，python中的range函数是左闭右开区间
            因此不需要对求幂的数进行减1的操作
    """
    def getval(self, val) -> list:
        num = 10 ** val
        ret = []
        for i in range(1, num):
            ret.append(i)
        return ret


if __name__ == '__main__':
    a = Solution()
    res = a.getval(3)
    print(res)
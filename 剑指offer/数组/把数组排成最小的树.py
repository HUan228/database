"""
输入一个非负整数数组numbers，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组[3，32，321]，则打印出这三个数字能排成的最小数字为321323。
1.输出结果可能非常大，所以你需要返回一个字符串而不是整数
2.拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

数据范围:
0<=len(numbers)<=100
"""
import functools


class Solution:
    """
    暴力破解：冒牌排序
    """
    def sortval(self, lis: list[int]) -> str:
        def sort_val(x, y):
            if x + y > y + x:
                return True
            else:
                return False
        nums = [str(i) for i in lis]
        for i in range(len(lis)):
            for j in range(len(lis) -i -1):
                if sort_val(nums[j], nums[j + 1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return ''.join(nums)


class Solution1:
    """
    python内置函数实现
    由于python3中不支持比较函数，cmp_to_key就是将老式的比较函数转化为关键字函数，
    与能够接收key function的函数一起使用，比如list, sort, sorted, min, max等
    """
    def sortval1(self, lis:list[int]) -> str:
        def sort_val1(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0
        nums = [str(i) for i in lis]
        nums.sort(key=functools.cmp_to_key(sort_val1))
        return ''.join(nums)


if __name__ == '__main__':
    a = Solution()
    b = Solution1()
    vet = [3, 32, 321]
    vet1 =[11, 3]
    print(a.sortval(vet1))
    print(b.sortval1(vet))

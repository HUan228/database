"""
输入一个递增排序的数组array和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，返回任意一组即可，如果无法找出这样的数字，返回一个空数组即可。

数据范围:
0<=len(array)<=105
1<=array[i]<=106
"""


class Solution:
    """
    解题思路，双指针法
    """
    def FindNumbersWithSum(self , array: list[int], sum: int) -> list[int]:
        # write code here
        i = 0
        j = len(array) - 1
        while i < j:
            if array[i] + array[j] > sum:
                j -= 1
            elif array[i] + array[j] < sum:
                i += 1
            else:
                return [array[i], array[j]]
        return []


if __name__ == '__main__':
    a = Solution()
    ret = [1, 2, 4, 7, 11, 15]
    target = 15
    print(a.FindNumbersWithSum(ret, target))
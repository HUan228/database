"""
输入一个长度为 n 整数数组，数组里面可能含有相同的元素，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，对奇数和奇数，偶数和偶数之间的相对位置不做要求，
但是时间复杂度和空间复杂度必须如下要求。

数据范围：0≤n≤50000，数组中每个数的值 0≤val≤10000
要求：时间复杂度 O(n)，空间复杂度 O(1)
"""


class Solution:
    def reOrderArrayTwo(self, array: list[int]) -> list[int]:
        # write code here
        left, right = 0, len(array) - 1
        while left < right:
            while left < right and array[left] % 2 == 0 and array[right] % 2 == 1:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
            while left < right and array[left] % 2 == 1:
                left += 1
            while left < right and array[right] % 2 == 0:
                right -= 1
        return array


if __name__ == '__main__':
    a = Solution()
    numbers = [1, 2, 3, 4]
    result = a.reOrderArrayTwo(numbers)
    print(result)
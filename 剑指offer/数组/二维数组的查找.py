"""
牛客网JZ4
在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
给定 target = 7，返回 true。
给定 target = 3，返回 false。
数据范围：矩阵的长宽满足 0 <= n, m≤500 ， 矩阵中的值满足 0≤val≤10^9
进阶：空间复杂度 O(1)，时间复杂度 O(n+m)
"""


class Solution:
    """
    解题思路：由于二维数组是有序的，在判断时可从行列入手，判断第一列最后一个值与目标值的大小，若比其大，则后退一列，
            若比其小，下移一行，逐步缩短查找的范围，最后返回相应的值
    """

    def IsExist(self, nums: list[list[int]], target: int) -> bool:
        if nums is None or nums[0] is None:
            return False
        row, col = len(nums), len(nums[0])
        left, right = 0, col - 1
        while 0 <= left < row and 0 <= right < col:
            if nums[left][right] > target:
                right -= 1
            elif nums[left][right] < target:
                left += 1
            else:
                return True
        return False


if __name__ == '__main__':
    val = Solution()
    ret = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    tar = 7
    result = val.IsExist(ret, tar)
    print(result)

"""
给定一个长度为 n 的非降序数组和一个非负数整数 k ，要求统计 k 在数组中出现的次数

数据范围：0≤n≤1000,0≤k≤100，数组中每个元素的值满足 0≤val≤100
要求：空间复杂度 O(1)，时间复杂度 O(logn)
"""


class Solution:
    """
    解题思路，1、字典 2、python自带函数count:data.count(k) 3、二分查找法
    """
    def GetNumberOfK(self , data: list[int], k: int) -> int:
        # write code here
        dic = {}
        for i in data:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        for key, v in dic.items():
            if key == k:
                return v
        else:
            return 0


if __name__ == '__main__':
    a = Solution()
    vet = [1, 2, 3, 3, 3, 3, 4, 5]
    target = 3
    print(a.GetNumberOfK(vet, target))
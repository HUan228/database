"""
给定一个数组 A[0,1,...,n-1] ,请构建一个数组 B[0,1,...,n-1] ,
其中 B 的元素 B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]（除 A[i] 以外的全部元素的的乘积）。
程序中不能使用除法。
（注意：规定 B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2]）
对于 A 长度为 1 的情况，B 无意义，故而无法构建，用例中不包括这种情况。

数据范围：1≤n≤10  ，数组中元素满足 ∣val∣≤10
"""


class Solution:
    def multiply(self, A: list[int]) -> list[int]:
        # write code here
        B = []
        for i in range(len(A)):
            val = A[:i] + A[i + 1:]
            data = 1
            for val_i in val:
                data *= val_i
            B.append(data)
        return B


if __name__ == '__main__':
    a = Solution()
    ret = [1, 2, 3, 4, 5]
    print(a.multiply(ret))
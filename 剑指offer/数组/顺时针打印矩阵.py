"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
"""
class Solution:
    def getnumber(self, array: list[list[int]]) -> list:
        if not array:
            return []
        l, r, t, b = 0, len(array[0])-1, 0, len(array)-1
        res = []
        while True:
            for i in range(0, r+1): res.append(array[t][i])
            t += 1
            if t > b: break
            for i in range(t, b+1): res.append(array[i][r])
            r -= 1
            if r < l: break
            for i in range(r, l-1, -1): res.append(array[b][i])
            b -= 1
            if t > b: break
            for i in range(b, t, -1): res.append(array[i][l])
            l += 1
            if l > r: break
        return res

"""
反转解压缩法：
class Solution:
    def getval(self, matrix: list[list[int]]) -> list:
        res = []
        while metrix:
            res += metrix.pop(0)
            matrix = list[zip(*metrix)][::-1] #解压缩并倒置
        return res
"""

if __name__ == '__main__':
    a = Solution()
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    result = a.getnumber(arr)
    print(result)
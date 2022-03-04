"""
JZ7
给定节点数为 n 的二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}

提示:
1.vin.length == pre.length
2.pre 和 vin 均无重复元素
3.vin出现的元素均出现在 pre里
4.只需要返回根结点，系统会自动输出整颗树做答案对比
数据范围：n≤2000，节点的值 −10000≤val≤10000
要求：空间复杂度 O(n),时间复杂度O(n)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def gettree(self, vin: list[int], pre: list[int]) -> TreeNode:
        if not pre or not vin:
            return
        rootnode = TreeNode(pre[0])
        root_index = vin.index(pre[0])
        rootnode.left = self.gettree(vin[:root_index], pre[1:1 + root_index])
        rootnode.right = self.gettree(vin[root_index + 1:], pre[root_index + 1:])
        return rootnode


if __name__ == '__main__':
    tree = Solution()
    prelist = [1, 2, 4, 7, 3, 5, 6, 8]
    vinlist = [4, 7, 2, 1, 5, 3, 8, 6]
    tree.gettree(vinlist, prelist)
    print(tree.gettree(vinlist, prelist))


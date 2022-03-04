"""
JZ8
给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。
树中从父节点指向子节点的指针用实线表示，从子节点指向父节点的用虚线表示

数据范围：节点数满足 1≤n≤50 ，节点上的值满足 1≤val≤100

要求：空间复杂度 O(1)，时间复杂度O(n)
输入描述：
输入分为2段，第一段是整体的二叉树，第二段是给定二叉树节点的值，后台会将这2个参数组装为一个二叉树局部的子树传入到函数GetNext里面，用户得到的输入只有一个子树根节点
返回值描述：
返回传入的子树根节点的下一个节点，后台会打印输出这个节点
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    """
    解题思路：
        对于求该节点中序的下一个结点，在中序中该结点的下一个结点必定是该节点右子树中左子树的叶节点
        若该结点是叶节点就返回它的父亲结点，并当该节点是父节点的左孩子时，父节点就是其下一个结点，
        若该节点是父亲结点的右节点，则继续向上查找，直到遇到该子树是某个结点的左子树为止
        否则该节点无下一个结点
    """
    def getroot(self, pNode) -> int:
        if not pNode:
            return pNode
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        while pNode.next:
            root = pNode.next
            if root.left == pNode:
                return root
            pNode = pNode.next

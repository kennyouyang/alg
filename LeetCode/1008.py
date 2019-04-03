#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.rank = 1

        def MakeNode(cur: TreeNode, pre: TreeNode):
            # left
            if self.rank < len(preorder) and preorder[self.rank] < cur.val:
                cur.left = TreeNode(preorder[self.rank])
                self.rank += 1
                MakeNode(cur.left, cur)
            if self.rank < len(preorder) and cur.val < preorder[self.rank] and (pre is None or preorder[self.rank] < pre.val):
                cur.right = TreeNode(preorder[self.rank])
                self.rank += 1
                MakeNode(cur.right, pre)
        root = TreeNode(preorder[0])
        MakeNode(root, None)
        return root

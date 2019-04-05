#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.string = list()

        def MakeString(node: TreeNode, back: str):
            full = chr(node.val + 97) + back
            if not node.left and not node.right:
                self.string.append(full)
            else:
                if node.left:
                    MakeString(node.left, full)
                if node.right:
                    MakeString(node.right, full)

        MakeString(root, '')
        return min(self.string)

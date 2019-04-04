#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def MakeNode(l, r) -> TreeNode:
            if l < r:
                v = max(nums[l:r])
                i = nums.index(v)
                n = TreeNode(v)
                n.left = MakeNode(l, i)
                n.right = MakeNode(i + 1, r)
                return n
            else:
                return None
        return MakeNode(0, len(nums))

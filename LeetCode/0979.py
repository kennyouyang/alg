#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:

        def ReadNode(n: TreeNode) -> (int, int):
            if n:
                ls, lm = ReadNode(n.left)
                rs, rm = ReadNode(n.right)
                m = lm + rm + n.val - 1
                s = abs(m) + ls + rs
                return s, m
            else:
                return 0, 0

        return ReadNode(root)[0]

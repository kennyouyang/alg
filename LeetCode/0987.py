#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import queue

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.pos = list()

        def MakePos(n: TreeNode, x: int, y: int):
            if n:
                self.pos.append((x, y, n.val))
                MakePos(n.left, x - 1, y + 1)
                MakePos(n.right, x + 1, y + 1)

        MakePos(root, 0, 0)
        vt = list()
        X = None
        for x, _, v in sorted(self.pos):
            if X != x:
                vt.append(list())
                X = x
            vt[-1].append(v)
        return vt

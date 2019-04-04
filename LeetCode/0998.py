#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def Copy(r: TreeNode) -> TreeNode:
            if r:
                n = TreeNode(r.val)
                n.left = Copy(r.left)
                n.right = Copy(r.right)
                return n
            else:
                return None

        def Add(r: TreeNode, v: int) -> TreeNode:
            if r:
                if r.val < v:
                    n = TreeNode(v)
                    n.left = Copy(r)
                    return n
                else:
                    n = TreeNode(r.val)
                    n.left = Copy(r.left)
                    n.right = Add(r.right, v)
                    return n
            else:
                return TreeNode(v)
        
        return Add(root, val)

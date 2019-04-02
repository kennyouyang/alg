#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # rank val
        top = list()
        larger = list()
        p = head
        r = 0
        while p:
            # to top
            if not top or top[-1][1] >= p.val:
                top.append((r, p.val))
                p = p.next
                larger.append(0)
                r += 1
            # to top
            else:
                i, _ = top.pop()
                larger[i] = p.val
        return larger

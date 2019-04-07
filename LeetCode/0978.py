#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        def cmp(a, b): return 0 if a == b else (-1 if a < b else 1)
        pre = 0
        cur = 0
        msize = 1
        size = 1
        for i in range(1, len(A)):
            cur = cmp(A[i-1], A[i])
            if pre * cur != -1:
                size = 2 if cur else 1
            else:
                size += 1
            msize = max(msize, size)
            pre = cur
        return msize

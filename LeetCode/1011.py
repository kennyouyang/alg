#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        def Check(full: int) -> bool:
            c = 1
            s = 0
            for w in weights:
                if s + w > full:
                    s = w
                    c += 1
                    if c > D:
                        return False
                else:
                    s += w
            return c <= D
        r = sum(weights) + 1
        l = max(max(weights), (r-1) // D) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if Check(m):
                r = m
            else:
                l = m
        return r

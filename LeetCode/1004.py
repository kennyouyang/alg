#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def longestOnes(self, A, K: int) -> int:
        zero = 0
        l = 0
        r = 0
        longest = 0
        while r < len(A):
            if A[r] == 0:
                if zero < K:
                    zero += 1
                    r += 1
                else:
                    if A[l] == 0:
                        zero -= 1
                    l += 1
            else:
                r += 1
            if zero <= K:
                longest = max(longest, r - l)
        return longest

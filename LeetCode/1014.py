#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        left = A[0]
        score = 0
        for r, v in enumerate(A[1:], 1):
            score = max(score, left + v - r)
            left = max(left, v + r)
        return score

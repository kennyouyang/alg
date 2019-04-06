#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        i, j = 0, 0
        interval = list()
        while i < len(A) and j < len(B):
            if A[i].end < B[j].start:
                i += 1
            elif B[j].end < A[i].start:
                j += 1
            else:
                interval.append(Interval(max(A[i].start, B[j].start), min(A[i].end, B[j].end)))
                if A[i].end < B[j].end:
                    i += 1
                elif A[i].end > B[j].end:
                    j += 1
                else:
                    i += 1
                    j += 1
        return interval

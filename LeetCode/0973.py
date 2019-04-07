#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def Eu(p):
            return p[0] ** 2 + p[1] ** 2

        def Partition(l, r):
            if l + 1 < r:
                p, q = l + 1, l + 1
                while q < r:
                    if Eu(points[q]) <= Eu(points[l]):
                        points[p], points[q] = points[q], points[p]
                        p += 1
                    q += 1
                if p > l + 1:
                    points[l], points[p - 1] = points[p - 1], points[l]
                return p - 1
            else:
                return l

        l, r = 0, len(points)
        while True:
            m = Partition(l, r)
            if m == K-1:
                return points[:K]
            elif m < K - 1:
                l = m + 1
            else:
                r = m

#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def camelMatch(self, queries, pattern: str):
        match = list()

        def Match(q: str, p: str):
            i, j = 0, 0
            while i < len(q):
                if j < len(p) and q[i] == p[j]:
                    j += 1
                elif 'A' <= q[i] and q[i] <= 'Z':
                    return False
                i += 1
            return i == len(q) and j == len(p)

        for q in queries:
            match.append(Match(q, pattern))
        return match


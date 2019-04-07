#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        div = {0:0}
        s = 0
        for a in A:
            s += a
            s %= K
            div.setdefault(s, 0)
            div[s] += 1
        sub = div[0]
        for v in div.values():
            sub += v * (v - 1) // 2
        return sub 

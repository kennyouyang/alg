#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import bisect


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        num = set()
        for i in range(len(S)):
            n = 0
            for j in S[i:]:
                n <<= 1
                n += int(j)
                num.add(n)
        if len(num) >= N:
            num = sorted(list(num))
            bl = bisect.bisect_left(num, N)
            return bl == N and num[bl] == N
        else:
            return False

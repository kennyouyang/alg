#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        # f(i) % k = 10 * f(i-1) % k + 1
        ones = 1
        for i in range(K):
            mod = ones % K
            if mod == 0:
                return i + 1
            else:
                ones = 10 * mod + 1
        return -1

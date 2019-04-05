#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        s = 0
        while X < Y:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            s += 1
        return s + X - Y

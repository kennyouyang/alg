#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def baseNeg2(self, N: int) -> str:
        def Step(n):
            if n != 0:
                mod = abs(n % -2)
                return Step((n - mod)//-2) + ('1' if mod else '0')
            else:
                return ''
        return Step(N) if N else '0'

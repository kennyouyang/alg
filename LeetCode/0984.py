#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        self.a, self.b = 'a', 'b'

        def MakeStr(a: int, b: int):
            if a == 0:
                if b > 0:
                    return MakeStr(a, b - 1) + self.b
                else:
                    return ''
            elif a == b:
                return MakeStr(a - 1, b - 1) + self.a + self.b
            else:
                return MakeStr(a - 1, b - 2) + self.a + self.b + self.b

        if A > B:
            self.a, self.b = self.b, self.a
            A, B = B, A
        return MakeStr(A, B)

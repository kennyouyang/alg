#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def isValid(self, S: str) -> bool:
        stack = list()
        for c in S:
            if c == 'a':
                stack.append(1)
            elif c == 'b' and stack and stack[-1] == 1:
                stack[-1] = 2
            elif c == 'c' and stack and stack[-1] == 2:
                stack.pop()
            else:
                return False
        return not stack

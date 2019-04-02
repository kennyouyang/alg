#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        r, c = len(A), len(A[0])
        out = [[False] * c for i in range(r)]
        todo = list()
        def Append(x, y):
            if A[x][y] == 1 and not out[x][y]:
                out[x][y] = True
                todo.append((x, y))
        #edge
        for i in range(max(r, c)):
            if i < r:
                Append(i, 0)
                Append(i, c - 1)
            if i < c:
                Append(0, i)
                Append(r-1,i)
        for x,y in todo:
            if x > 0:
                Append(x - 1, y)
            if x < r - 1:
                Append(x + 1, y)
            if y > 0:
                Append(x, y - 1)
            if y < c - 1:
                Append(x, y + 1)
        #check
        inner = 0
        for aa, oo in zip(A, out):
            for a, o in zip(aa, oo):
                if a == 1 and not o:
                    inner += 1
        return inner

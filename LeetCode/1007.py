#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def minDominoRotations(self, A, B) -> int:
        ta, tb = A[0], B[0]
        ra1, ra2, rb1, rb2 = 0, 1, 1, 0
        r = None
        ba, bb = True, True
        for a, b in zip(A[1:], B[1:]):
            if ba:
                if ta == a and ta != b:
                    ra2 += 1
                if ta != a and ta == b:
                    ra1 += 1
                ba = ta == a or ta == b
            if bb:
                if tb == a and tb != b:
                    rb2 += 1
                if tb != a and tb == b:
                    rb1 += 1
                bb = tb == a or tb == b
            if not ba and not bb:
                return - 1
        if ba:
            r = min(ra1, ra2)
        if bb:
            if r is None:
                r = min(rb1, rb2)
            else:
                r = min(rb1, rb2, r)
        return r

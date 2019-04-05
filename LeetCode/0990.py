#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def equationsPossible(self, equations) -> bool:
        ne = list()
        self.eq = dict()

        def Find(a):
            if a not in self.eq:
                self.eq[a] = a
                return a
            elif a == self.eq[a]:
                return a
            else:
                b = Find(self.eq[a])
                self.eq[a] = b
                return b

        for e in equations:
            if e[1] == '=':
                if e[0] != e[3]:
                    a = Find(e[0])
                    b = Find(e[3])
                    if a < b:
                        self.eq[b] = a
                    elif a > b:
                        self.eq[a] = b
            else:
                if e[0] == e[3]:
                    return False
                else:
                    ne.append((e[0], e[3]))

        for a, b in ne:
            if Find(a) == Find(b):
                return False
        return True

#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def clumsy(self, N: int) -> int:

        def Step4(N) -> int:
            if N >= 4:
                return N - (N-1) * (N-2) // (N-3) + Step4(N-4)
            elif N > 0:
                return 1
            else:
                return 0

        def Step3(N) -> int:
            if N >= 3:
                return N * (N - 1) // (N - 2) + Step4(N - 3)
            else:
                return N

        return Step3(N)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    def videoStitching(self, clips, T: int) -> int:
        if T == 0:
            return 0
        clips.sort()
        end = 0
        far = -1
        num = 0
        for i in clips:
            if i[0] <= end:
                far = max(far, i[1])
            elif i[0] <= far:
                num += 1
                end = far
                far = max(far, i[1])
            else:
                return - 1
            if T <= far:
                return num+1
        return -1

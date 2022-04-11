#!/bin/python
# -*- coding: utf-8 -*-

def jump_num(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    s1 = 1
    s2 = 2
    for i in range(3, n+1):
        num = s1 + s2
        s1 = s2
        s2 = num
        print i, num
    return num

if __name__ == '__main__':

    level = 10
    num = jump_num(level)
    print num


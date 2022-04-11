#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def get_largest_common_str(str1, str2):
    length1 = len(str1);
    length2 = len(str2);
    print length1
    print length2
    str_map = [0] * (length1 + 1)
    for i in range(0, length1 + 1):
        str_map[i] = [0] * (length2 + 1)
    max_num = 0
    max_start_idx = 0
    for i in range(0, length1):
        for j in range(0, length2):
            if str1[i] == str2[j]:
                str_map[i+1][j+1] = str_map[i][j] + 1
                if str_map[i+1][j+1] > max_num:
                    max_num = str_map[i+1][j+1]
                    max_start_idx = i + 1 - max_num
    for info in str_map:
        print info
    print "max common str num is " + str(max_num)
    print "max common str start idx in str1 is " + str(max_start_idx)
    return str1[max_start_idx:max_start_idx + max_num]

def get_largest_common_str_map(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    map_info = dict()
    for i in range(0, length2):
        if str2[i] not in map_info:
            map_info[str2[i]] = []
        map_info[str2[i]].append(i)
    max_num = 0
    max_start_idx = -1
    for i in range(0, length1):
        if str1[i] in map_info:
            for j in map_info[str1[i]]:
                num = 1
                m = i + 1
                n = j + 1
                while m < length1 and n < length2 and str1[m] == str2[n]:
                    m = m + 1
                    n = n + 1
                    num = num + 1
                if num > max_num:
                    max_num = num
                    max_start_idx = i
    if max_num <= 0:
        return ""
    return str1[max_start_idx:max_start_idx+max_num]

if __name__ == "__main__":
    str1 = "abcdcba"
    str2 = "dcbaabc"
    common_str = get_largest_common_str(str1, str2)
    #common_str = get_largest_common_str_map(str1, str2)
    print common_str


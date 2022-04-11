#!/bin/python
# -*- coding: utf-8 -*-

import copy

def get_largest_sub_list_length(nums):
    length = len(nums)
    if length <= 0:
        return 0
    if length == 1:
        return 1
    dp = [1] * length
    max_len = 1
    total_list = []
    for i in range(0, length):
        total_list.append([[nums[i]]])
    #print total_list
    max_list = []
    for i in range(1, length):
        for j in range(0, i):
            if nums[i] > nums[j] and dp[j] + 1 >= dp[i]:
                dp[i] = dp[j] + 1
                if dp[i] > max_len:
                    max_len = dp[i]
                for idx, temp_list in enumerate(total_list[j]):
                    if nums[i] <= temp_list[len(temp_list)-1]:
                        continue
                    #print j
                    #print total_list[j]
                    #print temp_list
                    new_list = copy.deepcopy(temp_list)
                    new_list.append(nums[i])
                    if len(new_list) >= max_len:
                        max_list = new_list
                    #print new_list
                    total_list[i].append(new_list)
                    #print total_list[i]
    print max_list
    print total_list
    for i in range(0, length):
        for j, temp_list in enumerate(total_list[i]):
            if len(temp_list) == max_len:
                print temp_list
    return max_len

if __name__ == '__main__':

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    #nums = [0, 1, 0, 3, 2, 3]
    length = get_largest_sub_list_length(nums)
    print length


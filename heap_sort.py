#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 堆排序：整体思想为升序排序构建大顶堆，降序排序构建小顶堆，将最大或者最小的值与堆中末尾值交换，然后将末尾节点从堆中摘除，重新构建堆，如此反复，直到参与建堆的节点数为0
# 将一个数组构建成一个满二叉树，假设父节点数组位置为i，则其左节点位置为 2*i+1 ，右节点位置为 2*i+2 ，如果数组长度为n，则最大一个非叶子节点的位置为 n/2-1 

def build_large_heap(arr, length):
    while True:
        adjust = False
        # 最大一个非叶子节点在数组中的位置
        start = length / 2 - 1
        for i in range(0, start + 1):
            # 从最大非叶子点开始，依次往顶端执行检测（大顶堆：每一个父节点的值都大于其孩子节点的值）
            parent = start - i
            left = parent * 2 + 1
            rigth = parent * 2 + 2
            # 取孩子节点中值较大的节点与父节点比较
            max_idx = left
            if rigth < length and arr[rigth] > arr[left]:
                max_idx = rigth
            if arr[max_idx] > arr[parent]:
                temp = arr[parent]
                arr[parent] = arr[max_idx]
                arr[max_idx] = temp
                adjust = True
        if not adjust:
            # 为了防止1轮调整完之后还是存在不满足大顶堆的情况，只要本轮存在调整，则再做一轮检测，直到无调整为止
            break
    return arr

def build_min_heap(arr, length):
    while True:
        adjust = False
        # 最大一个非叶子节点在数组中的位置
        start = length / 2 - 1
        for i in range(0, start + 1):
            # 从最大非叶子点开始，依次往顶端执行检测（大顶堆：每一个父节点的值都大于其孩子节点的值）
            parent = start - i
            left = parent * 2 + 1
            rigth = parent * 2 + 2
            # 取孩子节点中值较大的节点与父节点比较
            max_idx = left
            if rigth < length and arr[rigth] < arr[left]:
                max_idx = rigth
            if arr[max_idx] < arr[parent]:
                temp = arr[parent]
                arr[parent] = arr[max_idx]
                arr[max_idx] = temp
                adjust = True
        if not adjust:
            # 为了防止1轮调整完之后还是存在不满足大顶堆的情况，只要本轮存在调整，则再做一轮检测，直到无调整为止
            break
    return arr


def heap_sort(sort_arr, reverse = False):
    length = len(sort_arr)
    for j in range(0, length):
        if reverse:
            # 建立小顶堆
            build_min_heap(sort_arr, length - j)
        else:
            # 建立大顶堆
            build_large_heap(sort_arr, length - j)
        # 堆顶元素值与末尾元素值交换
        temp = sort_arr[0]
        sort_arr[0] = sort_arr[length - j - 1]
        sort_arr[length - j - 1] = temp

def quick_sort(arr, start, end):
    if start >= end:
        return 0
    temp = arr[start]
    i = start
    j = end
    while i < j:
        while i < j and arr[j] > temp:
            j = j - 1
        if i < j:
            arr[i] = arr[j]
        while i < j and arr[i] <= temp:
            i = i + 1
        if i < j:
            arr[j] = arr[i]
    arr[i] = temp
    quick_sort(arr, start, i-1)
    quick_sort(arr, i+1, end)
    return 0

def merge_sort(arr, start, end):
    if start >= end:
        return start, end
    mid = (start + end) / 2
    left_start_idx, left_end_idx = merge_sort(arr, start, mid)
    right_start_idx, right_end_idx = merge_sort(arr, mid+1, end)
    merge_list(arr, left_start_idx, left_end_idx, right_start_idx, right_end_idx)
    return left_start_idx, right_end_idx

def merge_list(arr, ls, le, rs, re):
    i = ls
    j = rs
    while i < j and j <= re:
        if arr[i] > arr[j]:
            temp = arr[j]
            s = j
            while s > i:
                arr[s] = arr[s-1]
                s = s - 1
            arr[i] = temp
            j += 1
        i += 1

if __name__ == '__main__':
    sort_arr = [4, 6, 8, 5, 9]
    #sort_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print sort_arr
    #heap_sort(sort_arr, True)
    #quick_sort(sort_arr, 0, len(sort_arr) - 1)
    merge_sort(sort_arr, 0, len(sort_arr) - 1)
    print sort_arr




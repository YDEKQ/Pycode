#! -*- coding:utf-8 -*-
#Python语言: 常见的排序算法实现与测速(Python)
# timing 7 different Python sorting algorithms with a list of integers
# each function is given the same list (fresh copy each time)
# tested with Python27     mac air i5       hey  

import random  # for generating random numbers
import time    # for timing each sort function with time.clock()

DEBUG = False  # set True to check results of each sort

N = 1000     # number of elements in list
list1 = []   # list of integer elements

for i in range(0, N):
    list1.append(random.randint(0, N-1))

#print list1  # test

def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

# declare the @ decorator just above each sort function, invokes print_timing()
@print_timing
# 系统自带sort()排序
def adaptive_merge_sort(list2):
    """adaptive merge sort, built into Python since version 2.3"""
    list2.sort()

@print_timing
# 冒泡排序 : 从这个数的下一个开始找，一直到末位，
# 看有没有比这个小的，如果有进行交换。
# 思路简单，运行较慢
def bubble_sort(list2):
    swap_test = False
    for i in range(0, len(list2) - 1):
        for j in range(0, len(list2) - i - 1):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]  # swap
            swap_test = True
        if swap_test == False:
            break

# selection sort
@print_timing
# 选择排序： 再左右2个数中选小的，进行交换
def selection_sort(list2):
    for i in range(0, len (list2)):
        min = i
        for j in range(i + 1, len(list2)):
            if list2[j] < list2[min]:
                min = j
        list2[i], list2[min] = list2[min], list2[i]  # swap
      
# insertion sort
@print_timing
# 插入排序： 在一个序列中插入一个数，找到比它大的那个数，
# 放在它前面，后面的数依次错一个。
# 这种方法相对稳定
def insertion_sort(list2):
    for i in range(1, len(list2)):
        save = list2[i]
        j = i
        while j > 0 and list2[j - 1] > save:
            list2[j] = list2[j - 1]
            j -= 1
        list2[j] = save
  
# quick sort
@print_timing
# 快速排序： 找到一个中间数，把比它小的数放在它的左边，比它大的放右边，
# 再对左右两边进行排序，以此类推。
# 这种方法速度块，但不稳定，最差的时候速度和上面两种方法一样。
def quick_sort(list2):
    quick_sort_r(list2, 0, len(list2) - 1)

# quick_sort_r, recursive (used by quick_sort)
def quick_sort_r(list2 , first, last):
    if last > first:
        pivot = partition(list2, first, last)
        quick_sort_r(list2, first, pivot - 1)
        quick_sort_r(list2, pivot + 1, last)

# partition (used by quick_sort_r)
def partition(list2, first, last):
    sred = (first + last)/2
    if list2[first] > list2 [sred]:
        list2[first], list2[sred] = list2[sred], list2[first]  # swap
    if list2[first] > list2 [last]:
        list2[first], list2[last] = list2[last], list2[first]  # swap
    if list2[sred] > list2[last]:
        list2[sred], list2[last] = list2[last], list2[sred]    # swap
    list2 [sred], list2 [first] = list2[first], list2[sred]    # swap
    pivot = first
    i = first + 1
    j = last
  
    while True:
        while i <= last and list2[i] <= list2[pivot]:
            i += 1
        while j >= first and list2[j] > list2[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            list2[i], list2[j] = list2[j], list2[i]  # swap
    list2[j], list2[pivot] = list2[pivot], list2[j]  # swap
    return j

# heap sort
# 堆排序： 将数据列成一个二叉树，比较子节和父节点，
# 如果子节点小于父节点，进行交换，以此类推。
# 这种方式速度块，稳定，编写难度大。
@print_timing
def heap_sort(list2):
    first = 0
    last = len(list2) - 1
    create_heap(list2, first, last)
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]  # swap
        establish_heap_property (list2, first, i - 1)

# create heap (used by heap_sort)
def create_heap(list2, first, last):
    i = last/2
    while i >= first:
        establish_heap_property(list2, i, last)
        i -= 1

# establish heap property (used by create_heap)
def establish_heap_property(list2, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and list2[k] < list2[k + 1]:
            k += 1
        if list2[first] >= list2[k]:
            break
        list2[first], list2[k] = list2[k], list2[first]  # swap
        first = k

# merge sort
@print_timing
def merge_sort(list2):
    merge_sort_r(list2, 0, len(list2) -1)

# merge sort recursive (used by merge_sort)
def merge_sort_r(list2, first, last):
    if first < last:
        sred = (first + last)/2
        merge_sort_r(list2, first, sred)
        merge_sort_r(list2, sred + 1, last)
        merge(list2, first, last, sred)

# merge (used by merge_sort_r)
def merge(list2, first, last, sred):
    helper_list = []
    i = first
    j = sred + 1
    while i <= sred and j <= last:
        if list2 [i] <= list2 [j]:
            helper_list.append(list2[i])
            i += 1
        else:
            helper_list.append(list2 [j])
            j += 1
    while i <= sred:
        helper_list.append(list2[i])
        i +=1
    while j <= last:
        helper_list.append(list2[j])
        j += 1
    for k in range(0, last - first + 1):
        list2[first + k] = helper_list [k]

# test sorted list by printing the first 10 elements
def print10(list2):
    for k in range(10):
        print list2[k],
    print


# run test if script is executed
if __name__ == "__main__" :
    print "timing 7 sorting algorithms with a list of 1000 integers:"
    # make a true copy of list1 each time
    list2 = list(list1)
    adaptive_merge_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    bubble_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    heap_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    insertion_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    merge_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    quick_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    selection_sort(list2)
    if DEBUG:
        print10(list2)
    # final test
    list2 = list(list1)
    if DEBUG:
        print "final test: ",
        print10(list2)

    #raw_input( "Press Enter to continue..." )

"""
typical results:
timing 7 sorting algorithms with a list of 1000 integers:
adaptive_merge_sort took 0.308ms
bubble_sort took 165.627ms
heap_sort took 7.676ms
insertion_sort took 82.485ms
merge_sort took 8.046ms
quick_sort took 4.934ms
selection_sort took 55.353ms

"""


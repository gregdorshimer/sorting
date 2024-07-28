# sorting
import math


def insertion_sort(my_list):
    """
    sorts my_list from least to greatest using insertion sort algorithm
    :param my_list: unsorted list of numbers
    :return: sorted list of numbers
    """
    if len(my_list) == 0:
        return my_list

    sorted_list = []

    # iterate over each item in the given list
    for insert_item in my_list:
        if len(sorted_list) == 0:
            sorted_list.append(insert_item)
        else:
            # insert the given item into the sorted_list
            sorted_list = insert(sorted_list, insert_item)
    return sorted_list


def insert(my_list, item):
    """
    inserts item into sorted my_list
    :param my_list: list sorted from least to greatest
    :param item: item to be inserted
    :return: sorted list that contains item
    """
    i = 0
    out_list = []
    while i < len(my_list):
        if my_list[i] < item:
            out_list.append(my_list[i])
            i += 1
        else:
            out_list.append(item)
            out_list.extend(my_list[i:])
            return out_list
    out_list.append(item)
    return out_list


def merge_sort(my_list):
    """
    sorts my_list from least to greatest using merge sort algorithm
    :param my_list: unsorted list of numbers
    :return: sorted list of numbers
    """
    if len(my_list) <= 1:
        return my_list

    first_half = my_list[:round(len(my_list)/2)]
    second_half = my_list[round(len(my_list)/2):]

    sorted_list = merge(merge_sort(first_half), merge_sort(second_half))
    return sorted_list


def merge(my_list1, my_list2):
    """
    merges two sorted lists into a single sorted list
    least to greatest
    :param my_list1: a sorted list
    :param my_list2: a sorted list
    :return: a sorted list containing all elements from both lists
    """
    combined_list = []
    i = 0
    j = 0
    # while loop continues as long as neither index has reached the end of its respective list
    while (i < len(my_list1)) & (j < len(my_list2)):
        # if the current element of my_list1 is less, then add it to the combined_list and advance in my_list1
        if my_list1[i] < my_list2[j]:
            combined_list.append(my_list1[i])
            i += 1
        # if the current element of my_list2 is less, then add it to the combined_list and advance in my_list2
        else:
            combined_list.append(my_list2[j])
            j += 1
    # once one of the indices has reached the end of its list, determine which has remaining items, and append only
    # those remaining items onto the combined_list
    if (i >= len(my_list1)) & ~(j >= len(my_list2)):
        combined_list.extend(my_list2[j:])

    if ~(i >= len(my_list1)) & (j >= len(my_list2)):
        combined_list.extend(my_list1[i:])

    return combined_list


# heapsort
def heapsort(my_list):
    # https://en.wikipedia.org/wiki/Heapsort
    """
    In-place sort of my_list using heapsort algorithm:
        (1) turns the list into a max-heap
        (2) sorts the max-heap into a sorted list
    :param my_list: the unsorted array
    :return: my_list after it has been sorted
    """
    # heapify my_list
    # call sift_down recursively on indices from len(my_list) / 2 to 0
    for i in range(math.floor((len(my_list) - 1) / 2), -1, -1):
        sift_down(my_list, i)

    # sort my_list by extracting the root n times and placing it at the end of my_list
    # for index i from len(my_list) - 1 to i = 0
    #   swap root last index of heap
    #   sift_down the root
    for j in range(len(my_list) - 1, 0, -1):
        temp = my_list[j]
        my_list[j] = my_list[0]
        my_list[0] = temp
        sift_down(my_list, 0)

    return my_list


# sift_down, helper for heapsort
def sift_down(my_heap, i):
    """
    Sifts the item at the given index down the given heap, in-place
    :param my_heap: a binary max-heap (it need not obey heap requirements as this function is used to re-heapify
    an altered heap)
    :param i: index of the item that needs to be sifted down
    :return: my_heap with item at index i sifted down through the heap
    """
    child_index1 = 2 * i + 1
    child_index2 = 2 * i + 2
    # if no child nodes:
    if child_index1 >= len(my_heap):
        # we have reached the bottom of the heap and no swap to be made, so return
        return my_heap
    # if there is one child node:
    elif child_index1 == len(my_heap) - 1:
        # compare, and swap if needed
        if my_heap[i] < my_heap[child_index1]:
            temp = my_heap[i]
            my_heap[i] = my_heap[child_index1]
            my_heap[child_index1] = temp
            return sift_down(my_heap, child_index1)
        # if no swap needed, then we are finished sifting down
        return my_heap
    # if there are two child nodes:
    else:
        # compare and swap with max(child1, child2) if needed
        if my_heap[child_index1] > my_heap[child_index2]:
            max_child_index = child_index1
        else:
            max_child_index = child_index2
        # compare to parent, swap if needed
        if my_heap[i] < my_heap[max_child_index]:
            temp = my_heap[i]
            my_heap[i] = my_heap[max_child_index]
            my_heap[max_child_index] = temp
            return sift_down(my_heap, max_child_index)
        else:
            return my_heap


# quicksort
def quicksort(my_list):
    # https://en.wikipedia.org/wiki/Quicksort#Algorithm
    """
    In-place sort of my_list using quicksort algorithm
    :param my_list: an unsorted list of type comparable by ==, <, >
    :return: my_list, after it has been sorted
    """
    # base case/continuation condition, covering lists of size 0, 1, 2
    if len(my_list) <= 1:
        return my_list
    elif len(my_list) == 2:
        if my_list[0] < my_list[1]:
            return my_list
        else:
            temp = my_list[0]
            my_list[0] = my_list[1]
            my_list[1] = temp
            return my_list

    # choosing pivot, median-of-three method
    first = my_list[0]
    middle = my_list[math.floor(len(my_list) / 2)]
    last = my_list[len(my_list) - 1]
    triple = [first]
    triple = insert(triple, middle)
    triple = insert(triple, last)
    my_list[0] = triple[0]
    my_list[math.floor(len(my_list) / 2)] = triple[1]
    my_list[len(my_list) - 1] = triple[2]
    pivot_index = math.floor(len(my_list) / 2)
    pivot_val = my_list[pivot_index]

    # swap pivot with last item in the list (this could be combined with steps above to shorten code)
    my_list[math.floor(len(my_list) / 2)] = my_list[len(my_list) - 1]
    my_list[len(my_list) - 1] = pivot_val

    # iterate over list from left and right, swapping items if they are on the wrong
    # side of the pivot
    index_from_left = 0
    index_from_right = len(my_list) - 2
    while index_from_left < index_from_right:
        # if both indices have found items that are out of place (larger or smaller than the pivot, respectively),
        # then swap them
        if (my_list[index_from_left] > pivot_val) & (my_list[index_from_right] < pivot_val):
            temp2 = my_list[index_from_left]
            my_list[index_from_left] = my_list[index_from_right]
            my_list[index_from_right] = temp2
            # increment/decrement both indices because a swap was done
            index_from_left += 1
            index_from_right -= 1

        # if left has found a val that needs to be swapped but right has not, then
        # decrement right and don't change left
        elif (my_list[index_from_left] > pivot_val) & (my_list[index_from_right] >= pivot_val):
            index_from_right -= 1

        # if right has found a val that needs to be swapped but left has not, then
        # increment left and don't change right
        elif (my_list[index_from_left] <= pivot_val) & (my_list[index_from_right] < pivot_val):
            index_from_left += 1

        # otherwise, neither index has found a value out of place, so increment/decrement both
        else:
            index_from_left += 1
            index_from_right -= 1

    # now swap the pivot back into the list at index_from_left, or index_from_left + 1, depending on
    # whether the item at index_from_left is larger or smaller than the pivot. This last check
    # accounts for cases where the indices overlap
    if my_list[index_from_left] > pivot_val:
        pivot_swap_index = index_from_left
    else:
        pivot_swap_index = index_from_left + 1

    temp3 = my_list[pivot_swap_index]
    my_list[pivot_swap_index] = pivot_val
    my_list[len(my_list) - 1] = temp3

    # now the pivot copied to index_from_left, so that
    # everything to the left of the pivot is smaller, and everything to the right of the pivot is larger
    # so recur on each half, and append the results with the pivot in between
    result = quicksort(my_list[:pivot_swap_index])
    result.append(pivot_val)
    result.extend(quicksort(my_list[pivot_swap_index + 1:]))
    return result


# searching an ordered list with a loop
def bin_search_loop(my_list, target):
    """
    Searches the given array for the target value, returns the index if found, -1 if not found
    :param my_list: a list of items of type comparable by '==', '>', and '<', sorted from least to greatest
    :param target: an item of type that matches items in my_list
    :return: index of target in my_list, if exists, or -1 otherwise
    """
    left = 0
    right = len(my_list) - 1

    while True:
        # if the list is size = 0, return -1 because target was not found
        if left > right:
            return -1

        # find the middle of the array, rounding down
        middle = math.floor((left + right) / 2)
        val = my_list[middle]
    
        # if the middle value is greater than the target, then the target would be in the left half
        if val > target:
            right = middle - 1

        # if the middle value is less than the target, then the target would be in the right half
        elif val < target:
            left = middle + 1
    
        # to arrive here, val must equal target, so return its index: middle
        else:
            return middle


# searching an ordered list with recursion (functional)
def bin_search_recur(my_list, target):
    """
    Searches the given array for the target value, returns the index if found, -1 if not found
    :param my_list: a list of items of type comparable by '==', '>', and '<', sorted from least to greatest
    :param target: an item of type that matches items in my_list
    :return: index of target in my_list, if exists, or -1 otherwise
    """
    return bin_search_recur_helper(my_list, target, left=0, right=len(my_list) - 1)


# helper for bin_search_recur
def bin_search_recur_helper(my_list, target, left, right):
    if left > right:
        return -1
    middle = math.floor((left + right) / 2)
    val = my_list[middle]

    # if the middle value is greater than the target, then the target must be in the left half
    if val > target:
        return bin_search_recur_helper(my_list, target, left, middle - 1)

    # if the middle value is less than the target, then the target must be in the right half
    elif val < target:
        return bin_search_recur_helper(my_list, target, middle + 1, right)

    # here, the middle value must equal the target, so return its index: middle
    else:
        return middle


list1 = [1, 4, 8]
list2 = [1, 2, 3, 4, 5]
list3 = []
list4 = [6, 6, 6, 6]
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list6 = [1, 2, 3, 5, 4]
list7 = [5, 3, 6, 8, 2, 4, 1, 9, 7]
list8 = [3, 5, 7, 9, 11, 13, 16, 20, 24, 30, 35, 100]
list9 = [11, 27, 23, 29, 33, 93, 62, 14, 8, 0, 123]

"""
print(insert(list1, 6))
print(insert(list2, 6))
print(insert(list3, 6))
print(insert(list4, 6))
print(insert(list5, 6))

print(insertion_sort(list2))
print(insertion_sort(list3))
print(insertion_sort(list6))
print(insertion_sort(list7))

print(merge([], [3]))
print(merge([3], []))
print(merge([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13]))
print(merge(list1, list4))

print(list1, ' sorted to ', merge_sort(list1))
print(list2, ' sorted to ', merge_sort(list2))
print(list3, ' sorted to ', merge_sort(list3))
print(list4, ' sorted to ', merge_sort(list4))
print(list5, ' sorted to ', merge_sort(list5))
print(list6, ' sorted to ', merge_sort(list6))
print(list7, ' sorted to ', merge_sort(list7))

print(bin_search_recur(list8, 3))
print(bin_search_recur(list8, 5))
print(bin_search_recur(list8, 16))
print(bin_search_recur(list8, 35))
print(bin_search_recur(list8, 100))
print(bin_search_recur(list8, 1))
print(bin_search_recur(list8, 25))
print(bin_search_recur(list8, 1000))

print(bin_search_loop(list8, 3))
print(bin_search_loop(list8, 5))
print(bin_search_loop(list8, 16))
print(bin_search_loop(list8, 35))
print(bin_search_loop(list8, 100))
print(bin_search_loop(list8, 1))
print(bin_search_loop(list8, 25))
print(bin_search_loop(list8, 1000))

print('list1 before: ', list1)
print('list1 after: ', quicksort(list1))
print('list3 before: ', list3)
print('list3 after: ', quicksort(list3))
print('list4 before: ', list4)
print('list4 after: ', quicksort(list4))
print('list6 before: ', list6)
print('list6 after: ', quicksort(list6))
print('list7 before: ', list7)
print('list7 after: ', quicksort(list7))
print('list9 before: ', list9)
print('list9 after: ', quicksort(list9))

# TODO test sift_down

print('list1 before: ', list1)
print('list1 after: ', heapsort(list1))
print('list3 before: ', list3)
print('list3 after: ', heapsort(list3))
print('list4 before: ', list4)
print('list4 after: ', heapsort(list4))
print('list6 before: ', list6)
print('list6 after: ', heapsort(list6))
print('list7 before: ', list7)
print('list7 after: ', heapsort(list7))
print('list9 before: ', list9)
print('list9 after: ', heapsort(list9))
"""

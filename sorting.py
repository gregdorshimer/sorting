# sorting

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
    if len(my_list) == 1:
        return my_list

    first_half = my_list[:round(len(my_list)/2)]
    second_half = my_list[round(len(my_list)/2):]

    sorted_list = merge(merge_sort(first_half), merge_sort(second_half))
    return sorted_list

def merge(list1, list2):
    """
    merges to sorted lists into a single sorted list
    least to greatest
    :param list1: a sorted list
    :param list2: a sorted list
    :return: a sorted list containing all elements from both lists
    """
    combined_list = []
    while((len(list1) > 0) & (len(list2) > 0)):
        if list1[0] < list2[0]:
            combined_list.append(list1[0])
            del list1[0]
        else:
            combined_list.append(list2[0])
            del list2[0]

    if (len(list1) == 0):
        combined_list.extend(list2)

    if (len(list2) == 0):
        combined_list.extend(list1)

    return combined_list




list1 = [1, 4, 8]
list2 = [1, 2, 3, 4, 5]
list3 = []
list4 = [6, 6, 6, 6]
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list6 = [1, 2, 3, 5, 4]
list7 = [5, 3, 6, 8, 2, 4, 1, 9, 7]

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
print(merge(list1, list4))

print(merge_sort(list1))
print(merge_sort(list2))
print(merge_sort(list3))
print(merge_sort(list4))
print(merge_sort(list5))
print(merge_sort(list6))
print(merge_sort(list7))
"""
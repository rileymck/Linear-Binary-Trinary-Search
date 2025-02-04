"""
Assignment 1: Linear, Binary, and Trinary Search  
Author: Riley McKenzie  

This program implements three search algorithms:  
1. Linear Search  
2. Binary Search  
3. Trinary Search
"""


from typing import List, Tuple
import time


def linearSearch(list_of_items: List[int], item_sought: int) -> Tuple[int, int, float]:

    item_index = -1
    number_comparisons = 0
    start_time = time.time()

     #Linear Search Implementation
    for index, item in enumerate(list_of_items):
        number_comparisons += 1
        if item == item_sought:
            item_index = index
            break
            
    elapsed_time = time.time() - start_time

    return (item_index, number_comparisons, elapsed_time)


def binarySearch(list_of_items: List[int], item_sought: int) -> Tuple[int, int, float]:
    item_index = -1
    number_comparisons = 0
    start_time = time.time()

    #Binary Search Implementation
    left, right = 0, len(list_of_items) - 1
    while left <= right:
        mid = (left + right) // 2
        number_comparisons += 1
        if list_of_items[mid] == item_sought:
            item_index = mid
            break
        elif list_of_items[mid] < item_sought:
            left = mid + 1
        else:
            right = mid - 1

    elapsed_time = time.time() - start_time       

    return (item_index, number_comparisons, elapsed_time)


def trinarySearch(list_of_items: List[int], item_sought: int) -> Tuple[int, int, float]:
    item_index = -1
    number_comparisons = 0
    start_time = time.time()

    #Binary Search Implementation
    left, right = 0, len(list_of_items) - 1
    while left <= right:
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third
        number_comparisons += 1

        if list_of_items[mid1] == item_sought:
            item_index = mid1
            break
        elif list_of_items[mid2] == item_sought:
            item_index = mid2
            break
        elif item_sought < list_of_items[mid1]:
            right = mid1 - 1
        elif item_sought > list_of_items[mid2]:
            left = mid2 + 1
        else:
            left, right = mid1 + 1, mid2 -1

    elapsed_time = time.time() - start_time

    return (item_index, number_comparisons, elapsed_time)



# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':

    def testFunction(search_function, alist, item):
        res = search_function(alist, item)
        print(f"\n{search_function.__name__} results")
        print(f"    input list size: {len(alist)}")
        print(f"    item sought: {item}")
        print(f"    item index: {res[0]}")
        print(f"    number of comparisons: {res[1]}")
        print(f"    elapsed time: {res[2]:.6f} seconds")

    # test functions with a list containing ~20 items
    list1 = [2, 3, 6, 10, 11, 17, 20, 23, 24, 29, 31, 34, 38, 39, 42, 47, 53, 71]
    item1 = 3
    testFunction(linearSearch, list1, item1)
    testFunction(binarySearch, list1, item1)
    testFunction(trinarySearch, list1, item1)

    # test functions with a list containing ~20 items and non-existent item
    list2 = [2, 3, 6, 10, 11, 17, 20, 23, 24, 29, 31, 34, 38, 39, 42, 47, 53, 71]
    item2 = 100
    testFunction(linearSearch, list2, item2)
    testFunction(binarySearch, list2, item2)
    testFunction(trinarySearch, list2, item2)

    # a list of odd numbers from 1 to 1e9
    list3 = list(range(0, int(5e6), 2))
    item3 = int(4e6)
    testFunction(linearSearch, list3, item3)
    testFunction(binarySearch, list3, item3)
    testFunction(trinarySearch, list3, item3)

    # a list of odd numbers from 1 to 1e8 with non-existent item
    list4 = list(range(1, int(1e7), 1))
    item4 = int(1e7)
    testFunction(linearSearch, list4, item4)
    testFunction(binarySearch, list4, item4)
    testFunction(trinarySearch, list4, item4)

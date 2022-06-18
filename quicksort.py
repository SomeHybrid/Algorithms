def binary_search(li, val, start, end):
    """
    An implementation of binary search customized for binary insertion sort.

    Time complexity: O(log n)
    Space complexity: O(log n)
    """
    if start == end:
        if li[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if li[mid] < val:
        return binary_search(li, val, mid + 1, end)
    elif li[mid] > val:
        return binary_search(li, val, start, mid - 1)
    else:
        return mid

def insertion_sort(li):
    """
    An implementation of binary insertion sort. This is similar to insertion sort but uses binary search.

    Time complexity:
     - Best case: O(n log n)
     - Worst case: O(n
    """
    for i in range(1, len(li)):
        val = li[i]
        j = binary_search(li, val, 0, i-1)
        li = li[:j] + [val] + li[j:i] + li[i+1:]
    return li

def median(l):
    """
    Gets the median of some elements
    """
    return insertion_sort(l)[len(l) // 2]

def quicksort(li):
    """
    An implementation of the quicksort algorithm.

    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(li) < 2:
        return li
    elif len(li) < 30:
        return insertion_sort(li)

    l = len(li) // 9
    items = [0] + list([l*x for x in range(7)]) + [l]
    i = items.index(median(items))
    pivot = li.pop(i)
    greater = []
    equal = []
    lesser = []
    for element in li:
        if element > pivot:
            greater.append(element)
        elif element < pivot:
            lesser.append(element)
        elif element == pivot:
            equal.append(element)
    return quicksort(lesser) + equal + quicksort(greater)

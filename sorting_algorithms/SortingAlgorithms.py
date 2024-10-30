# - Bubble sort: Repeatedly swaps adjacent elements 
# to "bubble" the largest unsorted element to its correct position.
def bubble_sort(l: list):
    for i in range(len(l)):
        swapped = False
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if not swapped:
            break
    return l

# bl = [2,5,6,8,9,4,2,7]
# bubble_sort(bl)
# print(bl)


# - Insertion sort: Builds a sorted portion of the list
#  by inserting elements one at a time.
def insertion_sort(l: list):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

# ins_list = [5,6,2,7,1,4,8]
# insertion_sort(il)
# print(il)



# - Selection sort: Repeatedly selects the smallest (or largest) element 
# from the unsorted portion and swaps it with the first unsorted element.
def selection_sort(l: list):
    for i in range(len(l - 1)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                l[j], l[min_index] = l[min_index], l[j]
    return l

# sl = [5,6,2,7,1,4,8]
# selection_sort(sl)
# print(sl)

# - Merge Sort: Divides the array into halves until each subarray has one element, 
# then repeatedly merges the subarrays back together in sorted order by comparing their elements.
def merge_sort(l: list):     
    pass

# ml = [2,5,6,8,9,4,2,7]
# merge_sort(ml)
# print(ml)

# - Quick Sort: Chooses a pivot element, rearranges the array so that elements less than the pivot come before it 
# and elements greater come after it, and then recursively applies the same process to the left and right subarrays.
def quick_sort(l: list):
    pass

# ql = [2,5,6,8,9,4,2,7]
# quick_sort(ql)
# print(ql)
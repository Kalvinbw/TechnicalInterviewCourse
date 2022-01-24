# Write a merge sort algorithm to sort an array. 
# The function should return the sorted array.

# two examples
array1 = [45, 98, 3, 24, 15, 77, 9, 50] # output: [3, 9, 15, 24, 45, 50, 77, 98]
array2 = [18, 16, 27, 4, 12] # output: [4, 12, 16, 18, 27]

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        
        l = array[:mid]
        r = array[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
  
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
    return array

merge_sort(array1)
merge_sort(array2)

print(array1)
# print(array2)

def binary_sort(array, n):
    l = 0
    r = len(array) - 1

    while l <= r:
        mid = (l+r)//2

        if n == array[mid]:
            return mid
        elif n > array[mid]:
            l = mid + 1
        elif n < array[mid]:
            r = mid - 1

    return -1

print(binary_sort(array1, 50))

def new_merge(a):
    if len(a) > 1:
        mid = len(a)//2

        l = a[:mid]
        r = a[mid:]

        new_merge(l)
        new_merge(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            a[k] = r[j]
            j += 1
            k += 1


new_merge(array2)
print(array2)

import timeit

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

arr2 = [2, 2, 1, 1, 1, 2, 2]
def findMaj(array):
    start = timeit.timeit()
    merge_sort(array)
    mid = len(array)//2
    end = timeit.timeit()
    print(end - start)
    return array[mid]


def findmajopt(array):
    start = timeit.timeit()
    my_counts = {}
    max = array[0]
    for item in array:
        if item in my_counts:
            my_counts[item] += 1
        else:
            my_counts[item] = 1
        
        if my_counts[item] > my_counts[max]:
            max = item

    end = timeit.timeit()
    print(end - start)
    return max


print(findMaj(arr2))
print(findmajopt(arr2))
# find common elements in 3 sorted arrays

l1 = [1,2,3,4]
l2 = [-2,-1,2,4,5,7]
l3 = [2,4,5,6,7,8,8,9]

# def helper(arr, di):
#     sub_counter = {}
#     for i in arr:
#         if i not in sub_counter:
#             # check if in counter
#             if i not in di:
#                 di[i] = 1
#             else:
#                 di[i] += 1


def helper(arr, di):
    for i in range(len(arr)):
        if arr[i-1] != arr[i]:
            # check if in counter
            if arr[i] not in di:
                di[arr[i]] = 1
            else:
                di[arr[i]] += 1

def find_common_elem(a1, a2, a3):
    # counter
    counter = {}
    # for each list
    helper(a1, counter)
    helper(a2, counter)
    helper(a3, counter)

    results = []
    # check the values in the counter
    for k, v in counter.items():
        if v == 3:
            results.append(k)
    
    return results


print(find_common_elem(l1, l2, l3))


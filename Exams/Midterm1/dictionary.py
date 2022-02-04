# Given a dictionary, sort the keys by the sum of their values in descending order. Return an array with the sorted pairs.

old_dict = { 'A' : [1, 2, 3], 'B' : [1, 7, 3], 'C' : [100, 3, 7], 'D' : [6, 50, 4]}
output = [['C', 110], ['D', 60], ['B', 11], ['A', 6]]

def sortDict(di):
    # sum the values in the original dictionary
    new_dict = {k:sum(v) for k, v in di.items()}
    # sort the dictionary
    return sorted(list(new_dict.items()), key=lambda x:x[1])[::-1]

print(sortDict(old_dict))

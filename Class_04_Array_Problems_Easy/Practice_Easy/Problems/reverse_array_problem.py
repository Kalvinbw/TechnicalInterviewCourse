# Write a function that reverses an array

input_array = [1, 2, 3, 4, 5, 6, 7, "a"]
# Output = ["a", 7, 6, 5, 4, 3, 2, 1]

def sort(array):
    n = []
    for i in range((len(array) - 1), -1, -1):
        n.append(array[i])
    return n
    
def mid(array):
    m = len(array) // 2
    for i in range(0, m):
        array[i], array[-i] = array[-i], array[i]
    return array


print(mid(input_array))
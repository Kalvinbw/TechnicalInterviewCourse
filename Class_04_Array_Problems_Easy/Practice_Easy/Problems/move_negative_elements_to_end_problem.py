# Write a function that moves all negative elements to the end of an array

input_array = [-1, 2, -3, 4, 5, 7]
# Output = [2, 4, 5, 7, -3, -1]

def move_neg(array):
    for i in range(len(array) - 1):
        if array[i] < 0:
            array.append(array.pop(i))

    return array

print(move_neg(input_array))

# Write a function that finds the missing number in an array

input_array = [1, 2, 3, 4, 6, 7]
input_array = [2, 3, 4, 6, 7]
# Output = 5

def find_missing(array):
    for i in range(len(array) - 2):
        if (array[i+1] - array[i]) > 1:
            return array[i] + 1


def opt(array):
    max = array[-1]
    length = len(array)

    v = ((max**2 + max))/2
    return v






print(opt(input_array))
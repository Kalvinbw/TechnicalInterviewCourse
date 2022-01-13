# Write a function that finds the minimum and maximum in an array 

input_array = [1, 2, 7, 9, -11, 10, 20, 1037]
# Output = -11, 1037

def find_min_max(array):
    min = array[0]
    max = array[0]
    for item in array:
        if item < min:
            min = item
        if item > max:
            max = item
    return min, max

def sorted(a):
    return a[0], a[len(a) - 1]

print(find_min_max(input_array))
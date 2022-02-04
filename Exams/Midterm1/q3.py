# Given a n x m binary matrix image, flip the image horizontally, then invert it, then return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0, 1, 1] results in [1, 0, 0].
# Examples:



from hashlib import new


Input =  [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
Output = [[1, 0, 0,], [0, 1, 0], [1, 1, 1]]
# Explanation:
# First reverse each row: [[0, 1, 1], [1, 0, 1], [0, 0, 0]]
# Then invert the image: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

def brute_force(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                arr[i][j] = 0
            else:
                arr[i][j] = 1

    return arr

def image_flip(arr):
    output = []

    for sub in arr:
        new_sub = []
        for i in range(len(sub)-1, -1, -1):
            if sub[i] == 1:
                new_sub.append(0)
            else:
                new_sub.append(1)
        output.append(new_sub)

    return output

# print(brute_force(Input))
print(image_flip(Input))
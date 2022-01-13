# You are given an m x n integer grid accounts where accounts[i][j]
# is the amount of money the ith customer has in the jth bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

input_accounts = [[2,8,7],[7,1,3],[1,9,5]]
# input_accounts = [[2,8],[7],[1,9,5]]
# input_accounts = [[2,8,7],[7,1,3],[1,9,5], [1]]
input_accounts = [[]]
input_accounts = []
# Output: 17

def rich(array):
    if len(array) == 0:
        return 0

    max = 0

    for p in array:
        money = sum(p)
        if money > max:
            max = money
    
    return max

print(rich(input_accounts))

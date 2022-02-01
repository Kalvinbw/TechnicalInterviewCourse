test_dict = {'B' : 4, 'Y' : 2, 'U' : 5}

def reverse(di):
    new_dict = {}
    keys = list(di.keys())

    for i in range(len(di) - 1, -1, -1):
        new_dict[keys[i]] = di[keys[i]]

    return new_dict

def opt(di):
    new_dict = {key:value for key, value in reversed(di.items())}
    return new_dict

print(reverse(test_dict))
print(opt(test_dict))

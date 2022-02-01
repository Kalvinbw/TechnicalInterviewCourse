test_dict = {'Manjeet' : [1, 4, 5, 6],
			'Akash' : [1, 8, 9],
			'Nikhil': [10, 22, 4],
			'Akshat': [5, 11, 22]}

def remove_dups(dict):
    myarr = []
    for v in dict.values():
        myarr.extend(v)
    print(myarr)
    
    counts = {}
    for v in myarr:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    
    for v in dict.values():
        for i in range(len(v)):
            if counts[v[i]] != 1:
                v.pop(i)
    
    return dict

print(remove_dups(test_dict))
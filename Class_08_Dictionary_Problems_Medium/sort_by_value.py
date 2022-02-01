from cgi import test


test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

def sort_values(di):
    new_dict = {}
    
    for k, sub_di in di.items():
        new_sub = {}

        for k, v in sub_di.items():
            min = ('English', sub_di['English'])
            for k2, v2 in sub_di.items():
                if v < min[1] and k2 != k:
                    min = (k, v)
        
            new_sub[k] = min[1]
        new_dict[k] = new_sub
    return new_dict

print(sort_values(test_dict))
        

def sortByValues(myDict):
    return {k:dict(sorted(v.items(),key=lambda kv:kv[1])) for k,v in myDict.items()}

print(sortByValues(test_dict))
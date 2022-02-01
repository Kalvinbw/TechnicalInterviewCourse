tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
  ("suraj", 20), ("akhil", 25), ("ashish", 30)]

def convert(array):
    myDict = {t[0]:t[1] for t in array}
    return myDict

print(convert(tups))
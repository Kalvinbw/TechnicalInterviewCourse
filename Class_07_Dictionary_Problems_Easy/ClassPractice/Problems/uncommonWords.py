s1 = 'this apple is sweet'
s2 = 'this apple is sour'

s3 = 'apple apple'
s4 = 'banana'


def uncommonWords(s1,s2):
    words = s1.split()
    words.extend(s2.split())
    unique = {}

    for word in words:
        if word not in unique:
            unique[word] = 1
        else:
            unique.pop(word)

    return list(unique.keys())

print(uncommonWords(s1,s2))
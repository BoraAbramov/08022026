
words = ["Dog", "cat", "Bird", "fish"]

    # print:
    #cat
    #fish

for item in words:
    if item[0].islower():
        print(item)

words = ["Apple", "banana", "Cherry", "date"]

    #print how much words start with capital

i = 0
for item in words:
    if item[0].isupper():
        i += 1

print(i)

words = ["Hi", "Hello", "Code", "Python"]

    #print words more than 4 charecters
for item in words:
    if item.__len__() > 4:
        print(item)

words = ["Hi", "Hello", "Code", "Python"]

    #print how much capital letters in every word
_length = 0

for item in words:
    item.split()
    if item.isupper():
        _length += 1
    print(_length)

list1 = ["HELLO", "World", "PYTHON", "code"]

for item in list1:
    if item.isupper():
        print(item[::-1])
    else :
        print(item)

    #if item.isupper():
    #   item = item[::-1]
    #   list_new.append(item)
    #else:
    #   list_new.append(item)
    #print(list_new)
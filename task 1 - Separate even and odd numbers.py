
list1 = [1, 2, 3, 4, 5, 6, 7]
list_even = []
list_odd = []

for item in list1:
    if item % 2 == 0:
        list_even.append(item)
    else:
        list_odd.append(item)

print(list_even)
print(list_odd)
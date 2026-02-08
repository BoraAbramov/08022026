#1
list1 = [1, 3, 5, 1, 7, 9, 2, 2, 8, 5, 10, 5]
list2 = [1, 2, 5]

for item in list2:
    while item in list1:
        list1.remove(item)

print(f"exercise 1 {list1}")

#2
list1 = [1, 2, 9, 88, 0]
list2 = [3, 4, -3]
list3 = [5, 6, 55]

list4 = []

for item in list1 + list2 + list3:
    list4.append(item)

print(list4)

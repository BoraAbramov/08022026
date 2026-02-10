
sentences = [
    "Hello world",
    "Python is fun",
    "I love coding"
]
list_s = []

for item in sentences:
    list_s.append (item.split())

print(list_s)

#almost solved

list_oreh = []

for item in sentences:
    list_oreh.append(item.__len__())

print(list_oreh)


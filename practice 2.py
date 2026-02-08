
grade_list: list[int] = []

while grade_list.__len__() < 10:
    grade = input("grade please")
    if grade.isdigit() and 0 <= int(grade) < 101:
        grade_list.append(int(grade))
    else:
        continue

_sum = 0
for item in grade_list:
    _sum += item
print(f"sum {_sum}")

_avg = _sum / grade_list.__len__()
print(f"avarage {_avg}")

print(f"the list {grade_list}")
grade_list.pop(9)
print(f"the list after pop 9 {grade_list}")

_min_grade = 100
_max_grade = 0
for item in grade_list:
    if item < _min_grade:
        _min_grade = item
    if item > _max_grade:
        _max_grade = item

grade_list.remove(_min_grade)

grade_list.insert(4, _max_grade)
grade_list.append(_max_grade)

print(f"minimum grade {_min_grade}, maximum grade {_max_grade}")
print(f"the list {grade_list}")


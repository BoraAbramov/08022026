
grade_list: list[int] = []

while grade_list.__len__() < 10:
    grade = input("grade please")
    if grade.isdigit() and 0 <= int(grade) < 101:
        grade_list.append(int(grade))
    else:
        continue

_sum = 0
for item in grade_list:
    _sum = _sum + item
print(_sum)

_avg = _sum / grade_list.__len__()
print(_avg)

grade_list.pop(9)

_min_grade = 100
_max_grade = 0
for item in grade_list:
    if item < _min_grade:
        _min_grade = item
    if item > _max_grade:
        _max_grade = item



print(_min_grade, _max_grade)
print(grade_list)


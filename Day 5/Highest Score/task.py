student_scores = [199, 142, 185, 120, 171, 184, 149, 24, 59, 68, 150, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

student_scores_max = 0
print(max(student_scores))
for mx_score in student_scores:
    if mx_score > student_scores_max:
        student_scores_max = mx_score
print(student_scores_max)

student = [1,2,3,4]
print(max(student))
Highest = 0
for i in student:
    if i >Highest:
        Highest = i
print(Highest)
# To find the lowest number we should compare with the first index of the list to find or use min
print(min(student))
lowest = student[0]
for i in student:
    if i <lowest:
        lowest = i
print(lowest)
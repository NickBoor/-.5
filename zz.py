score = [45, 60, 50, 90, 85]
grade = []

for i in range(0,5):
    if score[i]>=max(score)-10:
        value = "A"
    elif score[i]>=max(score)-20 and score[i]<max(score)-10:
        value = "B"
    elif score[i]>=max(score)-30 and score[i]<max(score)-20:
        value = "C"
    elif score[i]>=max(score)-40 and score[i]<max(score)-30:
        value = "D"
    else:
        value = "F"
    grade.append(value)

print(grade)


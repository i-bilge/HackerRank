from gettext import find


students = []

for i in range(int(input("Students: "))):
    name = input("name :")
    score = float(input("point: "))

    students.append([name,score])
    
print(students)
  
min = 100
second_Lowest_Students = []  
new_Scores = []  

for i in range(len(students)):
    if float(students[i][1]) <= min:
        min = float(students[i][1])  

for i in range(len(students)):
    if float(students[i][1]) == min:
        continue
    else:
        new_Scores.append(students[i][1])  
new_Scores.sort()        

for i in range(len(students)):
    if float(students[i][1]) == float(new_Scores[0]):
        second_Lowest_Students.append(students[i][0])  
second_Lowest_Students.sort()

print(*second_Lowest_Students, sep="\n")

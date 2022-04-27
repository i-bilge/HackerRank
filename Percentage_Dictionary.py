n = int(input("n:"))
student_marks = {}
for _ in range(n):
    line = input("x:").split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input("who:")

points = list(student_marks[query_name])

def percentage(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum+float(lst[i])
    return(float(sum/(len(lst))))        

answer = percentage(points)
print("{:.2f}".format(answer))




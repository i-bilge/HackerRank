x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
n = int(input("n:"))
    
first = [i for i in range(x+1)]
second = [j for j in range(y+1)]
third = [k for k in range(z+1)]
    
list = [first, second, third]
finallst=[]
sum = 0
print(list)
for i in first:
    for j in second:
        for k in third:
            sum = i+j+k
            if sum == n:
                continue
            else:
                finallst.append([i,j,k])

        
print(finallst)
    
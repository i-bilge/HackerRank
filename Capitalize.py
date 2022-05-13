def solve(s):
    l = s.split()

    for i in range(0,int(len(l))):
        if (l[i][0]).isalpha():
            l[i]=l[i].capitalize()
            i = i+1
        else:
            continue        
    print(*l)

s = input("isminiz? ")

print("the correct format :")
solve(s)

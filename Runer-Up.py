n = int(input("n :"))
arr = [2,3,6,6,5]

arr.sort()
max = -100
for i in arr:
    if i>max:
        max = i
m = arr.count(max)

print(arr[n-m-1])
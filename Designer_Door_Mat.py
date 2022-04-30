# Enter your code here. Read input from STDIN. Print output to STDOUT
# i am gonna hae 2 input: [N]line amount and [M]width(it s 3*line amount)
#then i have to organise the lines and columns according to middle of these
#and my figure has 3 elements: .|.
#rule of ".|."= 1:1,2:3,3:5,4:7...

N, M = map(int, input("line amount and width :").split())

for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))
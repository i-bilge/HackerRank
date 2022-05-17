# Input Format

# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

N = int(input("n :"))
Output = []
for i in range(0,N):
    ip = input().split()
    if ip[0] == "print":
        print(Output)
    elif ip[0] == "insert":
        Output.insert(int(ip[1]),int(ip[2]))
    elif ip[0] == "remove":
        Output.remove(int(ip[1]))
    elif ip[0] == "pop":
        Output.pop()
    elif ip[0] == "append":
        Output.append(int(ip[1]))
    elif ip[0] == "sort":
        Output.sort()
    else:
        Output.reverse()
'''
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
'''

def count_substring(string, sub_string):
    #string = string.lower()
    #string = string.replace(" ","")
    #sub_string = sub_string.lower()
    #sub_string = sub_string.replace(" ","")
    #m = len(sub_string)
    #n = len(string)
    x = 0
    #for i in range(0, n):
    #    if sub_string[0] == string[i]:
    #        x = x + (string[i:(i+m)].count(sub_string))
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            x += 1        
    return x


string = input("write the string :").strip()
sub_string = input("write the substring :").strip()
    
count = count_substring(string, sub_string)
print(count)
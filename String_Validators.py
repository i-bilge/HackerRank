'''
str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).
str.isdigit()
This method checks if all the characters of a string are digits (0-9).
str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).
str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).
'''
'''
You are given a string s.
Your task is to find out if the string s contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.
'''
s = input()
    
print(any(x.isalnum() for x in s))
print(any(x.isalpha() for x in s))
print(any(x.isdigit() for x in s))
print(any(x.islower() for x in s))
print(any(x.isupper() for x in s))
'''
How to wrap a text:
    WITH FILL
>>> import textwrap
>>> print(textwrap.fill(strs, 20))
    WITH WRAP
>>> import textwrap
>>> def wrap(string, max_width):
>>>     return '\n'.join(textwrap.wrap(string,max_width))
'''
'''
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.'''
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

string, max_width = input("write the string :"), int(input("give the width :"))
result = wrap(string, max_width)
print(result)
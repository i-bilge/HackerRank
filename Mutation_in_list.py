'''
>>> string = "abracadabra"
>>> print string[5]
a
-----------------------------
to assign a value
>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
How would you approach this?
One solution is to convert the string to a list and then change the value.
Example
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

Another approach is to slice the string and join it back.
Example
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
'''

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string


s = input("give the string :")
i, c = input("position and the character :").split()
s_new = mutate_string(s, int(i), c)
print(s_new)
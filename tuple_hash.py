integer_list = map(int, input("x").split())

integer_t = tuple(integer_list)
print(hash(integer_t))
# x = lambda a : a + 10
# print(x(2))


# # Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

#Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


soma = lambda x,y: (x + y)

results = soma(2, 8)

print(results)

printNames = lambda names: print(names)

printNames("Francisco Inoque")
#TODO: Number and String

#TODO: String

message = "Hello dude, my is Francisco Inoque and I have 2 computers." # => String

#TODO: Number

age = 27 # => Integer
height = 1.8 # => Float


#TODO: Aithmetic Operators

print(20 * 24 * 60)
print(20 + 20)
print(13- 7)
print(30/3)
print(30%3)


#TODO: String Concatenation

name = 'I am Francisco Inoque'
great = 'Hello, '
profession = ' a Software Developer and I am '
print(great + name + profession + str(27)+ ' years old.')


# Elegant Way
print('Elegant Way: ', f'{great} {name} {profession} {age} years old.')

# TODO: Lists
colors = ['Red', 'Blue', 'Yellow', 'White']

print(colors)


#TODO: Complex Type:
z = 1j  

print(type(z))

#TODO: Slicing Strings

b = "Hello, World!"
print(b[4:5])

#TODO: Modify Strings

a = "Hello, World!"
print(a.upper())

b = "Hello, World!"
print(a.lower())

#TODO: String Concatenation

c = "Hello"
d = "World"
e = c + d
print(e)

#TODO: Boolean

print(10 > 9) # Ttrue
print(10 == 9) # False
print(10 < 9) # False


a = 200
b = 33
c = b > a
if c != False:
  print("b is greater than a")
else:
  print("b is not greater than a")
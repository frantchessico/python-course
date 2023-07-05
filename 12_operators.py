#TODO: Arithmetic Operators

a = 5 + 7 #TODO: Addition
print("Addition: ",a)
b = 10 - 7 #TODO: Subtraction
print("Subtraction: ",b)
c = 4 * 6 #TODO: Multiplication
print("Multiplication: ",c)
d = 48 / 6 #TODO: Division
print("Division: ",d)
e = 40 / 8 #TODO: Modulus
print("Modulus: ",e)
f = 3 ** 3 #TODO: Exponentiation
print("Exponentiation: ",f)
g = 7 // 3 #TODO: Floor division
print("Floor division: ",g)

#TODO: Comparison Operators
#TODO: Equal:
x = 4
y = 5
if x == y:
    print(x + y)
else: print(False)


#TODO: Greater than
xx = 4
yy = 5
if xx > yy:
    print(xx + yy)
else: print(False)

#TODO:  Less than
xxx = 4
yyy = 5
if xxx < yyy:
    print(xxx + yyy)
else: print(False)

#TODO: Greater than or equal to 
xxxx = 4
yyyy = 5
if xxxx >= yyyy:
    print(xxxx + yyyy)
else: print(False)

#TODO:  Less than or equal to
xxxxx = 4
yyyyy = 5
if xxxxx <= yyyyy:
    print(xxxxx + yyyyy)
else: print(False)

#TODO: Not equal
xxxxxx = 4
yyyyyy = 5
if xxxxxx != yyyyyy:
    print(xxxxxx + yyyyyy)
else: print(False)


#TODO: Logical Operators


if(x < 5 and  x < 10): #TODO: Returns True if both statements are true
    print(True)
if(x < 5 or x < 4): #TODO: Returns True if one of the statements is true
    print(True)

if (not(x < 5 and x < 10)): #TODO: Reverse the result, returns False if the result is true
    print(True)

#TODO: Identity Operators

x = "Francisco"
y = "Francisco"

if(x is y):
    print("Is true")

if(x is not y):
    print("Make sense")


#TODO: Membership Operators

names = ["Francisco", "Inoque", "Jaime"]
name = "Francisco"
if(name in names):
    print(name)


if(name not in names):
    print(name)



thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "kiwi"
x = tuple(y)

print(x)



colors = ("red", "green", "black", "blue")
transform = list(colors)
transform[3] = "white"
trans = tuple(transform)
print(trans)

colors = ("red", "green", "black", "blue")
transform = list(colors)
transform.append("white")
trans = tuple(transform)
print(trans)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#TODO: Unpacking a Tuple

colors = ("red", "green", "black", "blue")

(red, green, black, blue) = colors
print(blue)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
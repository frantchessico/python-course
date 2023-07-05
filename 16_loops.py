i = 1
while i < 6:
    print(i)
    i += 1


i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

i = 1
while i < 8:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


for x in "banana":
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
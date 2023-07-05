thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#TODO: Add item Set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#TODO: Update set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


#TODO: Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


set_fruits = {"apple", "banana", "cherry"}
print(set_fruits)
del set_fruits

print("deleted")


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#TODO: Converts the first character to upper case
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#TODO: String casefold() Method Make the string lower case:

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

#TODO: String center Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"

x = txt.center(50)

print(x)


#TODO: COUNT: Returns the number of times a specified value occurs in a string

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

#TODO: ENCOD Returns an encoded version of the string

txt = "My name is Ståle"

x = txt.encode()

print(x)

#TODO: ENDSWITH: Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

#TODO: EXPANDTABS Sets the tab size of the string
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

#TODO: FIND: Searches the string for a specified value and returns the position of where it was found

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#TODO: FORMAT: Formats specified values in a string

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#TODO: INDEX: Searches the string for a specified value and returns the position of where it was found

txt = "Hello, welcome to my world."

x = txt.index("Hello")

print(x)

#TODO: JOIN: Joins the elements of an iterable to the end of the string

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#TODO: MARKTRANS: Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = str.maketrans("S", "F")
print(txt.translate(mytable))

#TODO: PARTITION: Returns a tuple where the string is parted into three parts

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

#TODO: REPLACE Returns a string where a specified value is replaced with a specified value

txt = "I like bananas"

x = txt.replace("bananas", "Francisco")

print(x)


#TODO: RFIND: Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa..."

x = txt.rfind("casa")

print(x)

#TODO: RSPLIT: Returns a right trim version of the string
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

#TODO: SPLIT: Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"

x = txt.split()

print(x)


txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)


txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)


txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)

#TODO: TRANSLATE: Returns a translated string

mydict = {83:  80}
txt = "Olá Francisco"
print(txt.translate(mydict))


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for list in list1:
    list2.append(list)

print(list2)
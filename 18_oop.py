# class MyClass:
#     x = 6


# result = MyClass().x
# print(result)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person = Person("Francisco", 27)

# print(person.age)

#TODO: Inheritance

class Person:
   def __init__(self, firstname, lastname):
      self.firstname = firstname
      self.lastname = lastname
   def printname(self):
      print(self.firstname, self.lastname)

person = Person("Francisco", "Inoque")
person.printname()

class Student(Person):
   pass

student = Student("Sara", "Rosa")
student.printname()

#TODO: Iterators

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
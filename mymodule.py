import camelcase
def greeting(name):
  print("Hello, " + name)


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

def showCamelCase(name):
  print(camelcase.CamelCase(name))

showCamelCase("Francisco Inoque")
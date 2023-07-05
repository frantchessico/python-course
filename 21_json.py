import json


person = {
    "name": "Francisco Inoque",
    "job": "Software Developer",
    "age": 27,
    "company": "SavanaPoint",
    "email": "franciscoinoque@savanapoint.com"
}


handlePerson = json.dumps(person);

jsonPerson = json.loads(handlePerson);

print(jsonPerson['email'])

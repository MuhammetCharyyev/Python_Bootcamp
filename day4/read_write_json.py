import json

path = 'files/Test.json'

jason_file = open(path, 'r')

dictionary = json.load(jason_file) # json.load will load data from the json file and assign to dict.

print(dictionary)
print(type(dictionary))

for x in dict(dictionary).keys():
    print(x) # getting every single keys in this dict

jason_file.close()

print('------------ Write Json file----------------------')

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },

    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },

    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

jason_file = open('files/Test2.json', 'w') # writing a new json file for adding above value

json_object = json.dumps(students, indent=3)  # converting dictionary object to json object

jason_file.write(json_object)

"""
Web Automation:
    BeautifulSoup4
    request
    pytest
    robot

Web Development:
    Django
    FastAPI
    flask
    ...
"""

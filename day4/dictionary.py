employee1 = {} # curly brases are especialy for dictionary (as Map in pair format)
# key is unique

employee1['name'] = 'James'
employee1['name'] = 'Daniel'
employee1['age'] = 45
employee1['salary'] = 60_000

print(employee1)

employee2 = { # dictionary as object
    'name': 'James',
    'age': 29,
    'salary': 80_000,
    'full_time': False
}

print(employee2)
print(employee2['name']) # print only one element

employee2['salary'] += 10000 # updating the value with adding
print(employee2)

employee2.update({'age': 40}) # update the exact key with a new value

print(employee2)

employee2['full_time'] = True

# employee2.update( {'full_time': True} )

print(employee2)

employee2.pop('full_time') # removing the entire pair

print(employee2)

# print( help(dict.popitem) )

employee2.popitem() #LIFO

print(employee2)

l = employee2.copy()

print(l)

print(employee2 is l) # return false

print('--------- Iterating Dictionary -----------------')

employee3 = {
    'name': 'Shay',
    'age': 29,
    'salary': 110_000,
    'full_time': False,
    'job_title': 'Developer',
    'company': 'Apple Inc'
}

print(list(employee3.keys())) # list all keys

for key in employee3.keys():
    print(f'{key} : {employee3[key]}') # iterate and concatenate a key and value

print('---------------------------------------')

values = list(employee3.values()) # list all values

print(values)

for value in employee3.values():
    print(value)

print('---------------------------------------')

for x in employee3.items():  # items(): returns a collection of tuples, in each tuple there will be two elements
    # print(x)
    print(f'{x[0]} : {x[1]}')
    # iterate and get each element as a tuple (x) but with concatenation and as a normal pair,
    #first element or key with index [0] and second element or value with index [1]

print('---------------------------------------')

students = {   # nested dictionary
    'A01': {   # ID 'A01" here is a key and the nested dictionary is a values
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

print(students)

students['A01']['gpa'] = 2.5 #accesing the exact element in the nested dictionary

print(students)

# students['A02'].update( {'name': 'Daniel' , 'gender': 'Male'} )
students['A02']['name'] = 'Daniel'
students['A02']['gender'] = 'Male'

print(students)

students['A03']['subjects'][1] = 'Biology' # access to exact element to the nested-nested dict. by index of List

print(students['A03'])

print('---------------------------------------------')


for x in students.items():
    print(x[1]) # getting the first inner dictionary
    for y in x[1]: # getting every single key in this internal dict.
        print(y)

print('---------------------------------------------')

for value in students.values(): # get all values
    print(value)
    for item in value.items(): # every single item in all nested dict.
        print(item[1]) # only values





from functools import reduce

print('------------------closure-----------------')


def display_message():
    def method(): #function calling inside the other function
        print('Hello World')
        print('I Love Python')

    method()
    method()
    method()
    method()


display_message()

print('------------')


def display_palindromes(strings: list):
    def is_palindrome(s: str) -> bool: # lambda here means a return type (boolean)
        return s[::-1].lower() == s.lower() # reverse the string with help of slicing

    for s in strings:
        if is_palindrome(s):
            print(s)


print('-----------------------map-------------')

nums = [10, 20, 30, 40, 50, 60, 70, 80]

nums = list(map(lambda x: x * 10, nums)) # lambda allows you to create a function wtht identifier
# x represents each element of nums

print(nums)

names = ['Java', 'JAVA', 'java', 'ruby', 'swift', 'CyDeO', 'javaSCRipt']

names = list(map(lambda s: str(s).upper(), names)) # transform each element of names to uppercase

print(names)

dictionary = {'x': 100, 'y': 200, 'z': 300}

dictionary = dict(map(lambda t: (t[0], t[1] * 10), dictionary.items())) # dictionary.items -> each object as tuple

print(dictionary)

print('--------------------filter------------------')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# nums = [ x for x in nums if x % 5 ==0]

nums = list(filter(lambda x: x % 5 == 0, nums)) # filter is literally making filtering

print(nums)


names = ['Java', 'JAVA', 'java', 'ruby', 'swift', 'CyDeO', 'javaSCRipt']

# names = [a for a in names if not a.lower().startswith('j')]

names = list( filter(lambda x: not str(x).lower().startswith('j'), names ))
# filtering and remove every string that starting with J

print(names)


print('--------------------reduce------------------')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print( reduce( lambda x, y: x+y , list1) ) # reduce elements to one value -> will return 45 as result


list2 = ['Java', 'Python', 'C#', 'Ruby']

print(  reduce( lambda x, y: f'{x} {y}' , list2 )  )
# reduce elements to one value -> will return one single string: Java Python C# Ruby


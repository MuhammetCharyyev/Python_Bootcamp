"""

Java Methods:
    public static void method(parameter){

    }


"""
import numbers


def display_message(): # def is a keyword of function
    print('Hello Cydeo')
    print('Hello World') # if you point return type as generic, then it will return as you point (str or int etc)


display_message()


def value():
    return 'Python Programming'


print(value())


def return_int() -> int: # point the specific return type, using a lambda
    return 10.0


print(return_int())


def square(num: int): # passing parameters in parentheses, specify data type (int) to avoid errors
    return num * num


print(square(10))


# print( square('Java'))

# print( divide('C#', 'Python'))

def add(num1: numbers, num2: numbers) -> numbers:
    # if you're not sure what is the data type for digits (int or float), then point 'numbers'
    return num1 + num2


print(add(10, 20))

print(add(10.5, 20.5))

print('------------------------------------------')


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    """
    An operator in Python is a special symbol that performs an action on one or more values.
     For example, the + operator adds two numbers, the * operator multiplies two numbers,
    and the / operator divides two numbers.
    """
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 20, '+'))

print(calculate(100.5, 2.5, '/'))

print('---------------------------------------------------------')


# example of method overloading

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    # we point '0' as e default argument in case of we do not point any parameters in a function
    # for this data, so these 2 will not be plus
    return n1 + n2 + n3 + n4


print(sum(10, 20))

print(sum(10, 20, 30))

print(sum(10, 20, 30, 40))


# PY method example
class test:
    def method(self):
        pass


print('----------------------------------------')


def concat(a: str, b, c='', d='', e=''): # default str arguments for the last 3 parameters
    # without default argument you must indicate parameters
    print(f'{a} {b} {c} {d} {e}'.strip()) # void type, no return type, if you dont want spaces, put .strip


concat('Cydeo', 'School')
concat('Python', 3, 2.5)
concat('Python', 3, 2.5, True)
concat('Python', 3, 2.5, True, False)


"""
1. Declaring
2. parameters
3. restricting parameter' data type
4. setting default value to parameter
5. restricting return type

Dynamic Typing
"""
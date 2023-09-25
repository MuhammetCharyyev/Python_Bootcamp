# arithmetic: +, -, *, /, %

print(10 - 2)
print(10 + 2)

print(10 * 3)

print(10 / 3) # will give a decimal as result but not int as in Java

print(10 / 2) # will give a decimal as result anyway

print(10 % 3) # will show you a remaining only as result

print(int(100 / 2)) # will give you int as result


# shorthand assignment operators: =, +=, -=, *=, /=, %=

a = 100

a = 200

print(a)


a += 100

print(a)

a -= 50

print(a)

a /= 2

print(a)


# logical operators: and, or, not
s = 'Hello World'

print('H' and 'W' in s) # checking if letters H and W are present in the str above

print(True and True)
print(True or False)

s = 'Java Python C# C++'

print( 'Java' or 'Ruby' in s) # checking if any of this words are present and revert back with 'Java'

age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'  # checking as IF statement

print(is_eligible)

has_java = 'Java' in s
print(has_java)

# !contains() in Java
print('Python' not in s)

print(not False)
print(not True)  # !

print('----------------------------------')

s = 'Java'
s2 = 'Java'

print( s is s2) # to heck if two variables are referencing to the same objects ( == operator of java)





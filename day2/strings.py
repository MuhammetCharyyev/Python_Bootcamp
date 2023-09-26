name = 'Python'

print(len(name)) # length of this string
print(name[0]) # first element
print(name[len(name) - 1]) # last element

print(name[-1]) # better way to get the last element (reverse index number)
print(name[-2]) # before the last element

s = 'Java Programming Language'
s2 = s[5:16] # slicing (like substring in Java), here we'll get "Programming"

print(s2)

s3 = s[:4] # slicing from the very beginning to the 4th element

print(s3)

s4 = s[::-1]  # reverses the string after slicing we'll get "egaugnaL gnimmargorP avaJ"

print(s4)

s = 'Python Programming'

s5 = str(reversed(s))

print(type(s5)) # will show the type as <class 'reversed'>
reversed(s5)

print(s5)

s5 = s[::-1]

print(s5)

s5 = 'python Programming'

s6 = s5[7:]  # by default it slices the string from index 7 to the last character

print(s6)


s7 = 'CYDEO SCHOOL'
# str(reversed(s7))

print('----------------------')

# print( help(str))


print('----------------------')

s = 'python programming language'

# s = s.capitalize() - will return with camel case for first word only
s = s.title() # will return with camel case for each word
print(s)

s = "            Python           "
s = s.strip()  # trim method of java, remove space

print(s)


s = 'JAVA'

print( s.index('A')) # index of first 'A'
print(s.rindex('A')) # last index of 'A'

s = 'Java Java'

s = s.replace('Java', 'Python', 1)

print(s)

s = 'C# C# Python'

s = s.replace(' C#', ' Java') # adding the space before C# point that we need to replace the second C3
print(s)


s = 'Java jAVA java JAVA Python Python'

count_java = s.lower().count('java') # count how many words, ignore case sensitivity
count_python = s.count('Python') # just count exact words

print(count_java)
print(count_python)


s1 = 'java'
s2 = 'JAVA'

print( s1.lower() == s2.lower())  # ignore case


s = 'Java'

print(s[0].islower()) # boolean, return FALSE
print(s[0].isupper() )


s = 'a'

print(s.isalpha()) # boolean, check if it's alphabetical

s = '1'

print(s.isdigit()) # boolean, check if it's numerical


s = 'Cydeo School'

print(s.istitle()) # boolean, check if all words with uppercase

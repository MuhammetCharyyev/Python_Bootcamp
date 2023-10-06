days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", 1, 2, 3, 4, 5, 6, 7, True, False)
# tuples like arrays in Java, but unchangeable,  consist many elements, divided by coma
print(type(days))
print(len(days))

print(days)

# days[0] = 'Java'
# print(days)


print(days[0])
print(days[-1]) # access to element of tuple by index

days = ('Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# work_days = days[1:-3]
work_days = days[1:4] # slicing of tuple by index: ('Tuesday', 'Wednesday', 'Thursday')
print(work_days)

week_days = days[:-2] # slicing tuple from the beginning to the element which is -2 from the end: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

print(week_days)

weekend = days[-3:] # slicing tuple from the element index -3 till the end: ('Friday', 'Saturday', 'Sunday')
print(weekend)

# == ,  'is'

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print( tuple1 == tuple2) # equal value
print( tuple1 is tuple2) # same object

tuple3 = tuple1 + tuple2 # simply merging 2 tuples
print(tuple3)

tuple4 = tuple1 * 5 # multiply of printing element but not value
print(tuple4)

reversed_tuple1 = days[::-1]

print(reversed_tuple1)

reversed_tuple2 = tuple(reversed(days)) # the other way to reverse tuple with 'reversed' method
print(reversed_tuple2)

print(days)

print(days.index('Wednesday'))

numbers = (10, 10, 10, 10, 20, 30, 40, 50, 10)

print( numbers.count(10) ) # counting all '10's

print('-------------------------')

for x in days: # for loop, print each element
    print(x)

print('-------------------------')

for x in range(0, len(days)): # index of each element of tuple
    print(x)


print('-------------------------')


for x in reversed(range(0, len(days))): # reversed index number
    print(x)

print('-------------------------')

nested_tuple = ( (1, 2, 3), (4, 5, 6, 7,8), (9, 10) ) # nested tuple is like multidimensional array

print(len(nested_tuple))

print('-------------------------')

for x in nested_tuple: # nested loop
    print(x)
    for y in x:
        print(y)

print('-------------------------')

for i in range(0, len(nested_tuple)):
    for j in range(0, len(nested_tuple[i])):
        print(nested_tuple[i][j])
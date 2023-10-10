groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken') # adding one element to the above list
groceries_list.extend(  ('Beef', 'Oranges', 'Onion') ) # extend above list with new elements

print(len(groceries_list))
print(groceries_list)

groceries_list[-2] = 'Cherry' # update above list at index -2 (second from the end)

print(groceries_list)

print('------------------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers_list)

numbers_list[2:-2] = [300, 4000, 5, 60000] # update above list from the index 2 till -2

print(numbers_list)

print('------------------------------------')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1 = characters[2: -3] # slicing above list from index 2 till -3 :- ['c', 'd', 'e', 'f']
print(list1)

list2 = characters[:4] # slicing from the very beginning till index -4
print(list2)

list3 = characters[2:] # slicing from the index till the end
print(list3)

characters[2:5] = ['C', "D", 'E', 'C', 'D', 'E', 'X', 'Y', 'Z'] # inserting in the interval from index 2 till 5

print(characters)

print('------------------------------------')

names = ['Conor', 'Steve', 'Hazel', 'Breanna']

for x in names: # iteration (loop) of each element
    print(x)

print('------------------------------------')

nums = [10, 20, 30, 40, 50, 60]

for i in range(len(nums)): # get range index numbers in above list from the very beginning (by default) till the end
    nums[i] = int(nums[i] / 5) # divide each element to 5 and assign it to int

print(nums)

print('------------------------------------')

nums = [10, 20, 30, 40, 50, 60]

for i in reversed(range(len(nums))):
    print(nums[i])

print('------------------------------------')

for x in nums[::-1]: # reversing with a help of slicing
    print(x)

print('------------------------------------')

for x in reversed(nums):
    print(x)

print('------------------------------------')

i = 0 # initiate and assign index to 'i' for while loop purpose

while i < len(nums):
    print(nums[i])
    i += 1

print('------------------------------------')

for i in range(1, 6):
    i += 2
    print(i)

print('------------------------------------')

nums = [60, 500, 10, 20, 15, 5, 0]

# nums.sort()  # ascending order

nums.sort(reverse=True) # sort list in descending (reversed) order

print(nums)

print('------------------------------------')

list1 = [10, 20, 30, 40]

# list1 = list( reversed(list1) )

list1.reverse()

print(list1)

print('------------------------------------')

tuple_elements = ('Java', 'Python', 'C#', 'Ruby')

list_elements = list(tuple_elements)
list_elements[-2] = 'C++'
list_elements.append('SWIFT')

print(list_elements)

tuple_elements = tuple(list_elements)

print(tuple_elements)

print('------------------------------------')

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

print(list1 is list2) # return FALSE because List is changeable

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)

print(tuple1 is tuple2) # return TRUE as tuple is immutable


print('------------------------------------')


groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef', 'Oranges', 'Onion'))

print(groceries_list)

groceries_list.remove('Beef')

print(groceries_list)

groceries_list.pop() # remove the last element in the list

print(groceries_list)

groceries_list.pop(1) # removing the 1 index from the list (second word)

print(groceries_list)

groceries_list.insert(2, 'Apple')
# insert VS append is when we want to insert at exact index number place

print(groceries_list)


print( groceries_list.index('Eggs'))

nums = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]

print(nums.count(1)) # count only '1' in the list


print('--------------- Comprehensions -------------------------')
# Comprehension is used to create a new List based on lists/set/tuples only and useful for filtering
# you may convert tuple to the list, make a comprehension and then convert back to the tuple

nums = []

for x in range(1, 50): # loop is a way to include elements (from 1 to 51) into the list without actual typing
    nums.append(x)

print(nums)

print('------------------------------------')

"""
divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x) # the one way to insert elements divisible by 5

print(divisible_by_5)
"""

divisible_by_5 = tuple( [ x  for x in nums if x % 5 == 0 ] )
# if you want to convert this list to tuple then use above construction

"""
the same way but shorter in 1 line using comprehension
to declare a comprehension always start with curlybrases of square brackets
first is a variable (x) that represent an element that will be inserted into the list
then it goes 'for' same variable name
'in' the existed list with elements
finally 'if' condition 

"""

print(divisible_by_5)

print('------------------------------------')

even_nums = [ x for x in nums if x % 2 == 0]
odd_numbers = [x for x in nums if x % 2 != 0]

print(even_nums)
print(odd_numbers)

print('------------------------------------')

names = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']

names = [x for x in names if x.lower() != 'java'] # comprehension to remove all javas

print(names)
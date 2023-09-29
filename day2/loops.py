
s = 'Python Programming'

for each in s:
    print(each) # will print each char of this string

print('-----------------------')

for i in range(0, len(s)): # iteration from 0 index till the length of this str
    print(s[i]) # if we keep just 'i' it will print index number, if we keep 's[i]' we'll get each char

print('-----------------------')

for i in range(-len(s), 0): # reverse iteration with negative sign
    print(s[i])

print('-----------------------')

for i in reversed( range(0, len(s)) ): # easiest way to get reverse
    print(s[i])

print('-----------------------')

result = ''

for x in s[::-1]: # iteration of shorted version
   result += x

print(result)

print('-----------------------')

for x in range(1, 11): # repeating 11 times of below
    print('Hello World')

print('-----------------------')

num = int( input('Enter a positive number:\n')) # input is like Scan in Java, will accept int only

while num <= 0: # while you dont enter positive number it will ask enter number
    num = int( input('Enter a positive number:\n'))

print(f'You have entered {num}')

print('-----------------------')

answer = input('Enter yes or no:\n')

while not ( answer.lower() == 'yes' or answer.lower() == 'no'): # 'lower' is for ignoring case
    answer = input('Enter yes or no:\n')

print(f'You have entered {answer}')
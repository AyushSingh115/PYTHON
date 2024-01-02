# make a list
from typing import List, Any

boys = ["ayush", "ashish", "akash"]
print(boys)

# get the first item in a list
print(boys[0])
# looping through a list
for boy in boys:
    print(boy)

# adding items to a list
boys.append("mohan")
print(boys)
# making numerical lists
numbers =[]
for num in range(1, 6):
    numbers.append(num)
    print(numbers)

 #other way

lamda= list(range(1,6))
print(lamda)
#List comprehensions
squares = [x**2 for x in range(1, 11)]
print(squares)
#or example of list comprehension
num=[number for number in range(1, 11)]
print(num)
print(num[:])
print(num[::-1])
print(num[-2:])


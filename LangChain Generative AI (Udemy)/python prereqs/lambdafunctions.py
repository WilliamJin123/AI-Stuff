#Syntax
# lambda arguments: expression
def addition(a,b):
    return a+b
addition = lambda a,b: a+b
print(addition(5,6))
def even(n):
    return True if n%2 == 0 else False
even1 = lambda n: n%2 == 0
print(even1(12))
def addition(x,y,z):
    return x+y+z
print(addition(12,13,14))
addition1 = lambda x,y,z: x+y+z
##map() - applies a function to all items in a list
numbers = [1,2,3,4,5,6]
def square(num):
    return num**2
print(list(map(lambda x:x**2, numbers)))

numbers = [1,2,3,4,5,6,7,8]

print(list(map(square, numbers)))

## Lambda function with map
print(list(map(lambda x:x*x, numbers)))

### Map multiple iterables 
numbers1 = [1,2,3]
numbers2 = [4,5,6]
added_numbers = list(map(lambda x, y: x+y, numbers1, numbers2))
print(added_numbers)

## map() to convert list of strings to integers
str_num = ['1','2','3','4','5']
int_num = list(map(int,str_num))
print(int_num)
## convert to uppercase
words = ['apple', 'cherry', 'banana']
upper = list(map(str.upper,words))
print(upper)

def get_name(person):
    return person['name']
people = [
    {'name': 'Krish', 'age':32},
    {'name': 'Jack', 'age': 33}
]
res = list(map(get_name, people))
print(res)

###FILTER FUNCTION
print(even(24))
lst = [1,2,3,4,6,7,8,9,10]
print(list(filter(even, lst))) #applies filter and returns elements that pass filter
#map would return boolean values

## filter with a lambda function
print(list(filter(lambda x:x>5, lst)))
print(list(map(lambda x:x>5, lst)))

## filter with a lambda function and multiple conditions
even_and_greater_than = list(filter(lambda x: x>5 and x%2==0, lst))
print(even_and_greater_than)

## filter() to check if age is greater than 25 in a dict
people = [
    {'name': 'Krish', 'age':32},
    {'name': 'Jack', 'age': 33},
    {'name': 'Jack', 'age': 25}
]
def age_greater_than_25(person):
    return person['age']>25
print(list(filter(age_greater_than_25, people)))
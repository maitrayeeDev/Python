#variables
x = 5
y = "John"
bool_var = True
print(x)

#receive input from user
name = input("Enter your name: ") #this will print the message and wait for user input and return what is entered
print("Hello, " + name)

#type conversion
birth_year = input("Enter your birth year: ") #will return value as string like "2002"
age = 2023 - int(birth_year) #convert the value and return value in integer datatype
print(age)

#conversion built-in function
#int()
#float()
#bool()
#str()

#sum of two numbers given by user
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
sum = first_num + second_num 
print("Sum of two numbers = " + str(sum))

#string operations
hello_world = "Hello World"
print(hello_world.upper()) #HELLO WORLD
print(hello_world) #Hello World

print(hello_world.find('l')) #return the first occurance of l in the string, if the character is not found it will return -1, we can also pass the substring in find method

print(hello_world.replace('World', 'Universe')) #replace the first argument with second argument in the string

#in keyword python
print('Hello' in hello_world) #return true if the first argument is present in the second argument else return false

#arithmetic operations
# / division operator
print(10 / 3) #3.3333333333333335, return full answer with floating points
print(10 // 3) #3, return only the integer part of the answer
print(2 ** 3) #8, return 2 to the power 3
#augmented assignment operator +=, -=, *=, /=, //=, **=, %=

#weight converter
weight = float(input("Enter your weight: "))
unit = input("Enter the unit (L)bs or (K)g: ")

if unit.upper() == 'L':
    converted_weight = weight/2.20462
    print("Weight in Kg = " + str(converted_weight))
elif unit.upper() == 'K':
    converted_weight = weight * 2.20462
    print("Weight in Lbs = " + str(converted_weight))

# * with string and integer
i = 5
print(i * 'A') #will print 'AAAAA'

#lists
courses = ['IT', 'ICT']
print(courses[-1]) #will print the last element of the list
print(courses[-2]) #will print the second last element of the list

#list operations
courses.append('CS') #add element to the end of the list
courses.insert(4, 'CS') #add element to the specified index of the list
print(courses)
courses.remove('CS') #remove the element from the list
courses.clear() #remove all the elements from the list
#in operator also works in list also
print(len(courses)) #return the length of the list

print(courses[0:2]) #will print the elements from index 0 to 1, 2 is excluded
print(courses[:2]) #same as upper line

#for loop
#item is loop variable
for item in courses:
    print(item) #will print all the elements of the list

i = 0
while i < len(courses):
    print(courses[i])
    #i++ #python does not support i++ or i-- operator
    i = i + 1

#range function
#we can also iterate over a range of numbers with range function
numbers = range(5, 10)
for number in numbers:
    print(number) #will print 5 to 9

numbers = range(5, 10, 2)
for number in numbers:
    print(number) #will print 5 to 9

#tuples
#tuples are immutable, we can not change the values of tuples
numbers = (1, 2, 3)
numbers[0] = 20 #this will give error

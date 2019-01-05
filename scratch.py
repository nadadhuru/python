
# define variables for data type int, float, string, boolean
height = 5.4
weight = 152
weight_unit = "lbs"
is_male = True

# use of literals like /, /n in printing

# use of + symbol for printing variable values and concatenation

# use of input method to collect input from user and need for converting text to number when needed
user_name = input("Enter user id:")
user_pwd = input("Enter your password")
age = input("Enter your password")
weight = input("Enter your weight in lbs")

#using available functions based on Variable type like String, Number etc
case_val = user_name.upper().isupper()
print(case_val)

# converting text to Number while printing variable value based on User Input & also for addition operation on user input value
int(variable) or floar(variable)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

# converting number (height) to text while printing next to text

# converting a number from int to float

# converting a number from float to Int

# Rounding a number to lower value when value is <0.5

# Rounding a number to higher value when value is > 0.5

# floor - - for rounding up to lower value despite what is next to .

# ceil - for rounding up to higher value despite what is next to .

# Power function - 4,6 = 4096 (4 x 4 x 4 x 4 x 4 x 4)

# Squareroot (sqrt) function - 36 = 6

# max

# min

# absolute function --> -5 to 5

# add, subtract, multiply, and divide numbers and set operation precedence

# mod operator

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

# length of a string

# find index of a letter/word in a given string using []

# find letter in a given string using .index()

# replace function to replace text in a file using -  .replace(sourcevalue, destinationvalue)

# Create a Triangle shape

# Create a Square shape

# Create a round shape

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

# Working with Lists - use this when we are using large amount of data

subject_list = ["Maths", "Science", "Social", "English", "Hindi"]
students_list = ["pavan", "mothey", "yugi", "kota"]
print(variable)

#access value of  lists using index
print(variable[index])

#using negative value for Index to print list values from last(-1) to first (-?)
print(variable[index])

#querying all values from a particular index using index:
print(variable[startingindex:])

#querying range of values from a particular index till endindex-1
print(variable[startingindex:endindex])

#modifying element value of a list
variable = ["a", "b", "c", "d"]
variable[2] = "e"
print(variable[])

#using functions with lists
students_list = ["pavan", "mothey", "yugi", "kota"]
students_id = [1, 2, 3, 4]

#add one list to another list by extending
students_list.extend(students_id)

#append a value and it will be added at the end of list
students_list.append("raj")

#add a value at particular index
students_list.insert(1, "sridhar")

#remove a particular value from list
students_list.remove("sridhar")

#removing all values from list
students_list.clear()

#removes last value in the list
students_list.pop()

#check if a value present in list and its index. If value is not present then we will error out
students_list.index("pavan")

#count similar elements in a list
students_list.append("pavan")
students_list.count("pavan")

#sort list - default ASC
students_list.sort()

#sort list - DESC or in reverse order
students_list.reverse()

#copying a list
students_attendance = students_list.copy()


# Learn TUPLES - its a type of Data Structure and its a container and store multiple values
# TUPLE is immutable means cant be modified or changed or add or remove elements - What you see is What you get
# syntax - variable = ()
gps = (4, 5)

#access TUPLE via index
gps = (4,5)
print(gps[1])

#Using Functions in Python
#Collection of code to do a specific task
#Identify tasks
#functions start with keyword - def

def hi():
    print("hi")

#accessing function
hi()

#parameterized function
def hi(name):
    print("hi" +name)

#access function
hi("pavan")

#return statement in a function. It wont execute any statement after return keyword
def add_numbers(num1, num2):
    sum1 = num1 + num2
    return(sum1)

#accessing function
add_numbers(2,4)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#If & If else Statement
is_male = True
if is_male :
    print("Yes")
else:
    print("No")

# Conditional If or If else  Statement
is_male = True
is_tall = True

if is_male or is_tall:
    print("Yes Male or Yes Tall or both")
else:
    print("You are not Male or Tall")

if is_male and is_tall:
    print("Yes you are Male and Tall")
else:
    print("You are either Male or Tall")

if is_male and is_tall:
    print("Yes you are Male and Tall")
elif is_male and not(is_tall):
    print("You are male and short")
else
    print("You are not a male or not tall")

# comparision operators will result in TRUE or FALSE
# >, <, >=, <=, ==, !=, and, or

def max_num(n1, n2, n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else
        return n3

#calling above function should return us 209
max_num(45, 209, 2)

#Excercise build a calculator that performs +, -, *, /, % for a given 2 numbers by user as User Input.
#Also collect the operator (+, -, *, /, %) from User via User Input

# Dictionaries in Python
# Dictionary is a special Structure in Python and allow us to store data in Key Value Pair format
# We use Key to access Values and Key must be unique. Keys can be text or numbers
# Exercise convert a 3 letter month to a full month name

monthConversion = {
    "Jan"   :   "January",
    "Feb"   :   "February",
    "Mar"   :   "March",

}

#Accessing Dictionary using key
print(monthConversion["Mar"])
print(monthConversion.get("Mar"))

#Passing a default value when no key matches
print(monthConversion.get("Apr", "This is not a valid Key"))


#While Loop in Python. One of the structure in Python that is used to execute a task/tasks until certain condition is false
#Heavy use in Games

num1 = 10
while num1 >=1:
    print(num1)
    num1 = num1-1
print("Exited Loop")

num2 = 1
while num2 <=10:
    print(num2)
    num2 += 1
print("Exited Loop")

#Excercise - Build a Guessing Game using Loops, Variables
# Program should store a secret word and user should try to guess


#For loop in Python. One of the structures in Python. This is used to execute a task/tasks until certain condition is false
for letter in "pavan":
    print(letter)

for students_list in students_list:
    print(students_list)

for i in students_list:
    print(i)

for i in range(len(students_list)):
    print(students_list(i))

for i in range(5):
    if i==0:
        print("This is 1st iteration")
    else:
        print("Not a 1st iteration")

#Exponent (Power function) Function using for loop
def exp_raise(base_number, power_number):
    result=1
    for i in range(power_number):
        result = result * base_number
    return result
print(exp_raise(2,3))

#2D Lists
student_name = ["Pavan", "Mothey", "Yugi", "Kota"]
students_id = {2,4,6,8}
students_id_2d = [[2,3,4], [5,6,7], [8,9,10], [11]]

print(students_id_2d[2][1])

#Nested for loop

for row in students_id_2d:
    for col in row
        print(col)

#Translation
def translation_fun(phrase):
    translation = ""
    for i in phrase:
	    if i in "AEIOUaeiou":
	    translation=translation + "g"
        else:
	    translation=translation+ i
    return translation
print(translation_fun("Test")

#Comments
#How to use comments in Python
print("Following msg will be commented out")
#print("This will be commented out")

'''
The lines in this section will be commented out
Including this line
'''

#Catching Errors using Try Except
# In this we will catch general error using except statement
# for specific exceptions specify the error type so that we will know what caused it
# you can also store the error message in a variable and print it out

try:
#    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero Error")
#except ValueError:
 #   print("Invalid Input")
except ValueError as verror:
    print(verror)

#Reading from external files using Python
# check if the file is readable
# First step is to open the file in read mode using relative path when the file is in same folder as Python
# print the info from file
# closing the file


employee_file = open("employees.txt", "r")
employee_file.redable()
employee_file.read()
employee_file.readline()
employee_file.readlines()
employee_file.close()

# First step is to open the file in write mode using relative path when the file is in same folder as Python
employee_file = open("employees.txt", "w")
employee_file.writable()
employee_file.write()
employee_file.writelines()
employee_file.close()

# First step is to open the file in append (adding at the end and not modify/changing anything) mode using relative path when the file is in same folder as Python
employee_file = open("employees.txt", "a")
employee_file.writable()
employee_file.write()
employee_file.writelines()
employee_file.close()

# First step is to open the file in  read & write mode using relative path when the file is in same folder as Python
employee_file = open("employees.txt", "r+")
employee_file.close()


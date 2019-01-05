'''

def greatest_number(a, b, c):
    if (a>=b) and (a>=c):
        print("Value of A is higher than B and C and the value is: " + str(a))
    elif(b>=a) and (b>=c):
        print("Value of B is higher than A and C and the value is: " + str(b))
    elif(c>=a) and (c>=b):
        print("Value of C is higher than A and B and the value is: " + str(c))
    else:
        print("Useless")

a = input("Enter value of A : ")
b = input("Enter value of B : ")
c = input("Enter value of C : ")

greatest_number(a, b, c)

monthConversion ={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(monthConversion["Mar"])
print(monthConversion.get("Mar"))
print(monthConversion.get("Apr", "No Key match found "))

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



guess_word = input("Enter an Animal starts with 'C' and ends with 'T': ")
guess_count = 1

while guess_word.upper() != "CAT":
    if guess_count < 5:
        print("Please guess again")
        guess_word = input("Enter an Animal starts with 'C' and ends with 'T':")
        guess_count += 1
    else:
        print("Sorry you have exceeded maximum no of guesses")
        break
if guess_count <5:
    print("Congrats you guessed the word and you have used " + str(guess_count) + " guesses to find correct one")


try:
    a = int(input("This is a test number - please provide a number: "))
    result = []
    while a > 0:
        if a%2 == 0:
            result.append(a)
        a= a-1
    print(sorted(result, reverse=False))
except ZeroDivisionError:
    print("Divided by Zero Error")
except ValueError:
    print("Invalid Input")
#result.sort()
#print(result)
#result.reverse()
#print(result)

for i in range(5):
    if i==0:
        print("This is 1st iteration")
    else:
        print("Not a 1st iteration")

for letter in "pavan":
    print(letter)

for i in "MOTHEY":
    print(i)

students_list = [1, 2, 3, "pavan", 4, 5]

#for i in students_list:
#    print(i)

for i in students_list[2:4]:
    print(i)

#for i in range(len(students_list)):
#    temp = students_list(i)
#    print(temp)

#Exponent (Power function) Function using for loop
def exp_raise(base_number, power_number):
    result=1
    for i in range(power_number):
        result = result * base_number
    return result
print(exp_raise(2,3))


try:
    rows = int(input("Enter how many rows you want to print: "))
    iteration = 1

    while(rows>=1):
        j = iteration
        while(j>0):
            print("*")
            j = j-1
        rows = rows - 1
        iteration += 1

except ValueError as e:
    print(e)

print("This is 2nd line")


students_id_2d = [[2,3,4], [5,6,7], [8,9,10], [11]]
print(students_id_2d[2][1:3])
#print(students_id_2d[2][2])

# Reading file
#open(employee.txt, )
from builtins import ValueError



#Identify how to make this dynamic. Yes - just add [] to same list
emp_data = []
r = int(input("How many rows of data you have?: "))
c = int(input("How many columns of data you have?: "))
i = 0
j = 0
for i in range(r):
    emp_data += [[]]
    print(emp_data)
    for j in range(c):
        emp_data[i].append(int(input("Enter your value:")))
print(emp_data)

qr = int(input("which row you want to search? "))
qc = int(input("which column you want to search?"))

if(qr<r and qc<c):
    print(emp_data[qr-1][qc-1])
else:
    print("Your search range is out of bound")

#Now ask user how many rows and how many columens he want and
# ask for a value along with Row and col number

user_data = []
r = int(input("How many rows of data you have?: "))
c = int(input("How many columns of data you have?: "))
i = 0
j = 0

for i in range(r):
    user_data += [[]]
    for j in range(c):
        user_data[i].append("")

er = int(input("Which row do you want to insert into: ? "))
ec = int(input("Which column do you want to insert into: ? "))
#uval = int(input("What is the value? "))

if(er<=r and ec<=c):
    user_data[er-1].insert(ec-1, input("What is the value? "))
else:
    print("Range is out of bound")

print(user_data)
'''

# Build a table with value from 1 to 100 and seek user input
# Search for the value in Table and display result (Present or Not Present)

math_data = []
r = int(input("Enter how many rows you want in your table?:  "))
c = int(input("Enter how many columns you want in your table?:  "))
i = 0
j = 0
cnt = 0
for i in range(r):
    math_data += [[]]
    for j in range(c):
        cnt+=1
        math_data[i].append(cnt)
print(math_data)
s_value = int(input("enter a search value:  "))

#print(math_data.index(s_value))
matchcount = 0

for i in range(r):
    for j in range(c):
        if(math_data[i][j] == s_value):
            matchcount += 1
            print("Found it, located at index: " + str(i+1) + " Row and " + str(j+1) + " Column")
            print("Value at that index is: " + str(math_data[i][j]))

if(matchcount==0):
    print("No value found, please try again")

#print(len(math_data))
#what is xrange?

open("employee.txt","r+")

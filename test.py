'''from math import *

print("This is a test program")
emp_id = input("Please enter your Employee ID: ")
emp_name = "Pavan"
emp_address = "2611 Mahogany Dr"

print("Employee ID is : " +str(emp_id))

print(emp_name.upper())
print("Employee Name is : " +emp_name + "\n")

print(emp_address.lower())
print("Employee Address is: " +emp_address)

print(len(emp_address))
print("This is a \"\"")

num1=-7.2
print(abs(num1))
print(int(num1))
m = 10%3
print(10%3)
print(m)
print(fmod(10,3))'''

print("Here is your Christmas tree...!! Yay..!!\n")

print("    *   ")
print("   ***   ")
print("  *****  ")
print(" ******* ")
print("**********")
print("    *   ")
print("    *   ")

student_id = [1,2,3]
student_name = ["Pavan", "Mothe", "Yugi"]

student_id.extend(student_name)
print(student_id)
student_name.append("Pavan")
#print(student_name.count("Pavan"))

student_no = [1, 34, 2, 98, 103, 6]
print(student_no)

#student_no.sort()
#print(student_no)


y = sorted(student_no, reverse=False)

print(y)
student_no.append(10)
x = sorted(student_no, reverse=True)
print(x)


#student_no.reverse()
#print(student_no)


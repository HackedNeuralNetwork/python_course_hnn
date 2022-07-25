"""
User input: Get Data From User
input() : String

*******Important *******
input(),type(),id() ==> Functions
name,address = Small Letter ( Variable )
Name = First letter Capital ( Class )

*********** Important Convert *************
string 'A' not convert into number
string '1' convert into number using int() ==> 1
string '56.5' convert into float using float() ==? 56.5
"""

name = input("Enter Your Name Here: ")
age = int(input("Enter Your Age Here: "))  # String to int
company_name = input("Enter Your Company Name: ")
mobileNumber = input("Enter Your Mobile Number: ")
mobileNumber = int(mobileNumber) # String to int

print("Name:- ",name)
print("Age:- ",age)
print("Company Name:- ",company_name)
print("Mobile Number",mobileNumber)
print(type(age),age)
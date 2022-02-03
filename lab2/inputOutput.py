#Author: David Sarkisian
#Assignment: Lab #2 part 2
#Completed: 02/02/2022

name = input("Please enter your name: ")
age = input("Please enter your age: ")
company = input("Enter the company you wish to work for: ")
salary = input("Enter monthly salary you wish to earn in dollars: ")
salary = int(salary) * 12


print("My name is", name, end = "")
print( ", my age is ", age, "\nI hope to work for", company, "and earn $", end = "") 
print(salary, "a year.")


#####OUTPUT#####
'''
#####OUTPUT #1#####
My name is Alice Wonderland, my age is  20 
I hope to work for Google  and earn $96000 a year.


#####OUTPUT #2#####
My name is David Sarkisian, my age is  222 
I hope to work for Deloitte and earn $78000 a year.
'''


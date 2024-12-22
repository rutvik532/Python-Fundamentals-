'''#1).Introduction to Python Theory
#1.1)Write a Python program that prints "Hello, World!".
print("Hello,World!")
#1.2)Set up Python on your local machine and write a program to display your name. 
name=input("Enter Your Name:")
print("Name:",name)


#2).Programming Style 
#3. Core Python Concepts
a=int(input("Enter number for square:"))
n=a*a
print("Square of Enter number:",n)
print(type(n))


#4. Conditional Statements 
4.1)Practical Example 5: Write a Python program to find greater and less than a number using 
if_else. 
a=int(input("Enter a number A for checking number is greater or less:"))
b=int(input("Enter a number B for checking number is greater or less:"))
if a>b :
    print("Number A is greater")

else :
    print("Enter number B is Greater ")

#4.2) Write a Python program to check if a number is prime using if_else.
a=int(input("Enter a number for checking the number is prime or not:"))

if a>1 :
    for i in range(2,int(a**0.5)+1) :
        if  a%i ==0 :
            print("Enter number is not prime number!")
        else :
            print("Enter number is prime number")

else :
    print("Enter number ia not a prime number")


4.3)Write a Python program to calculate grades based on percentage using 
if-else ladder. 
stu_name=input("Enter a student name:")
per=int(input("Enter a student percentage:"))

print("-"*50)
print("Student Name:",stu_name)
if per>=80 :
    print("Grade:A")

elif per>=70 :
    print("Grade:B")

elif per>=60 :
    print("Grade:C")


elif per>=40 :
    print("Grade:D")

else :
    print("Better luck next time:")

 4.4)Write a Python program to check if a person is eligible to donate blood 
using a nested if.
name=input("Enter a person Name:")
age=int(input("Enter person age:"))
blood_group=input("Enter person blood group:")

if age>=18 :
    if blood_group == "A"or blood_group == "B" :
        print("You are eligible for Blood Donation")

    else :
        print("Oops!You are not eligible for blood donate")

else :
    print("Ooops! You are not eligible for blood donate")

5.)looping Statement 

r=int(input("Enter the lanth of row:"))
c=int(input("Enter a column lenght:"))

for i in range(r) :
    for j in range(i) :
        print("*",end=" ")
    print()

Write a Python program to print each fruit in a list using a simple for 
loop. List1 = ['apple', 'banana', 'mango'] 

List1 = ['apple', 'banana', 'mango'] 

for i in List1 :
    print(i)
    print(f"lengh:{i}=",len(i))

#Write a Python program to find the length of each string in List1.
search=input("Enter a fruit name for search:")

if search in List1 :
    print("Your searching is found")
        
        
else :
    print("Oops try another time!")



7). Functions and Methods 
Practical Example: 1) Write a Python program to print "Hello" using a string. 
• Practical Example: 2) Write a Python program to allocate a string to a variable and print it. 
• Practical Example: 3) Write a Python program to print a string using triple quotes. 
• Practical Example: 4) Write a Python program to access the first character of a string using 
index value. 
• Practical Example: 5) Write a Python program to access the string from the second position 
onwards using slicing. 
• Practical Example: 6) Write a Python program to access a string up to the fifth character. 
• Practical Example: 7) Write a Python program to print the substring between index values 1 
and 4. 
• Practical Example: 8) Write a Python program to print a string from the last character. 
• Practical Example: 9) Write a Python program to print every alternate character from the 
string starting from index 1. 

str1="Hello"
print(str1)
print('Hello')
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[0:6])
print(str1[1:6])
print(str1[-6:])

8. Control Statements (Break, Continue, Pass) 
Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue 
statement. List1 = ['apple', 'banana', 'mango'] 
• Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using 
the break statement. 

List1 = ['apple', 'banana', 'mango'] 


for i in List1 :
    if i=="banana":
        continue
     print(i)


List1 = ['apple', 'banana', 'mango'] 


for i in List1 :
    if i=="banana":
        break
    print(i)


9.) String Manipulation 

Write a Python program to demonstrate string slicing. 
• Write a Python program that manipulates and prints strings using various string methods.

str1="We are learning python"

print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.count("a"))
str2=" We are learning python"
print(str2.strip())
print(str1.replace("python","coding"))
print(str1.split())'''


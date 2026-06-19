# Practice Set — Variables, Types, Operators

# vaiables + types 
name = "rajesh"
age = 30 
target_lpa = 60.0
committed = True
print("my name:",name,"age of:",age,"my target lpa:", target_lpa,"committed:",committed)

# All arithmetic operators
a = 29
b = 4
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)

#Type casting (input)
num1 = input("enter first number")
num2 = input("enter second number")
print("sum =:", int(num1) + int(num2))

#Even or odd check
print("2026 is even:", 2026 % 2 == 0)

#Comparison + logical
age = 34 
comitted = True 
print(age >= 18 and comitted == True)

# f-string sentence
name = "rajesh"
target_lpa = 60.0
committed = True
print(f"my name is {name}, my target lpa is {target_lpa} and i am committed:{committed}")
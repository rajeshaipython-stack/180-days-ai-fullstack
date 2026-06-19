 # Project block 
celsius = float(input("enter temperature in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degree celsius is  equal to {fahrenheit} degree fahrenheit")

# project block 2 if / elif / else
print (" === Temperature convertor ===")
print("1. celsius to fahrenheit")
print("2.fahrenheit to celsius:") 

choice = input("enter your choice:")
if choice == "1":
    celsius = float(input("enter temperatue in celsius:"))
    fahrenheit = (celsius * 9/5) + 32 
    print(f"{celsius}°C = {fahrenheit}°F")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 /9
    print(f"{fahrenheit}°F = {celsius}°C")
else:
   print("invalid choice, please select  1 or 2")
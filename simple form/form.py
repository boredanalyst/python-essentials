## This is a simple and basic form.

print("---FORM---")
print("Please fill out the details required.")
print("-------")

fName = input("FIRST NAME: " )
lName = input("LAST NAME: ")
age = int(input("AGE: "))
print("--------")
print(f'{fName} {lName}, age: {age}')
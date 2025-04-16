grades = [12,23,41,23,45,32,35,9,22]

print(grades)

new_grades = [grade + (grade * 0.10) for grade in grades]

print("10%+ of the grades.")
print(new_grades)

print("-----")

print("Only provide bonus to the grades above 30")

new_grades = [grade + (grade * 0.10) for grade in grades if grade >= 20]
print(new_grades)
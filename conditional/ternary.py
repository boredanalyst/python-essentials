

willGetbonus = True
firstGrade = 80

bonusGrade = 0.05 if willGetbonus else 0

print(f'Final Grade: {(firstGrade * bonusGrade) + firstGrade:.2f}')
a = 120
b = 130
c = 140

taxable = True

if (a > b) and (taxable == True):
    print(f'The total amount is ${a + b:.2f}')
elif (c > b) and (taxable == True):
    print(f'The total amount is ${c + b:.2f}')
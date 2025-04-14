## This is a basic calculator

print('Please provide your numbers.')
fNum = input("What is your first number?: ")
print(f'You chose {fNum}')
sNum = input("What is your second number?: ")
print(f'You chose {sNum}')


print('----------------')
print('What do you want to do?')
print(' 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division')

action = input("Please provide the number of your choice: ")
fNum = int(fNum)
sNum = int(sNum)



if int(action) in [1, 2, 3, 4]:
    if int(action) == 1:
        print(fNum + sNum)
    elif int(action) == 2:
        print(fNum - sNum)
    elif int(action) == 3:
        print(fNum * sNum)
    elif int(action) == 4:
        print(fNum / sNum)
else:
    print("Please retry.")



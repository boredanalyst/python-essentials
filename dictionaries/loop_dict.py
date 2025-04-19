myInfo = {
    "fName" : "Angel",
    "lName" : "Santos"
}

for key in myInfo:
    print("----")
    print(key)
    print(myInfo[key])

for key, value in myInfo.items():
    print(f'{key} = {value}')
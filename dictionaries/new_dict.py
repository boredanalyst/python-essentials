## Here we're creating a new dictionary from lists.

studentNames = ["Angel","Albert","Amir"]
studentAge = [12,14,13]

studentDict = {}

for x in range(len(studentNames)):
    print(studentNames[x])
    print(studentAge[x])
    studentDict.update({studentNames[x] : studentAge[x]})

print(studentDict)
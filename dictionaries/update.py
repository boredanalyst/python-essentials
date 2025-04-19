myInfo = {
    "fName" : "Angel",
    "lName" : "Santos"
}

print(myInfo["fName"])
print(myInfo["lName"])

myInfo.update({"fName" : "Mario"}) # This updates the value of an existing key.
myInfo.update({"age":24}) # This adds another key-value pair.


print(myInfo)
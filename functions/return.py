## A return line in a function allows a function to output a value

def adds(*args):
    addends = list(args)
    sum = 0
    for item in addends:
        sum += item
    return sum

sum = adds(1,4,5,6,2,4,3,4,5,1.5)

print(sum)
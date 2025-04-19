## Here's a function that uses a optional number of parameters.

def summation(*args):
    addends = list(args)
    sum = 0
    for item in addends:
        sum += item
    print(sum)

summation(2,3,5)
summation(99,99)
summation(1.2,2.3,4.4,7.5,6.6)
## Import the libraries
import random as rand


## Declare the list and numbers
first_number = 0
second_number = 0
numbers = [1,2,3,4,5,6,7,8,9]

## declare the variables for the results
result = ""
player_points = 0


## Function for getting the input of the player.
def inputAnswer():
    answer = ""
    while answer == "":
        answer = input("What is your guess? HIGH or LESS?: ")
        if answer == "HIGH" or answer == "LESS":
            print(f"You have chosen: {answer}")
            return answer
        else:
            print("Please choose either 'HIGH' or 'LESS'")
            answer = ""


## Randomize index and get the number
def randomize():
    rand_index = rand.randint(0,8)
    rand_number = numbers[rand_index] ## Store the number got from the list.
    return rand_number


## The function for comparing the previous number and the next one.
def compareNumbers():
    if first_number < second_number:
        print(f"The first number: {first_number} is LESS than the second number: {second_number}.")
        return "LESS"
    elif first_number > second_number:
        print(f"The first number: {first_number} is GREATER than the second number: {second_number}.")
        return "HIGH"
    else:
        print(f"The first number: {first_number} is EQUAL TO the second number: {second_number}.")
        return "EQUAL"

## The function that compares the player response and the result
def compareResults():
    if player_answer == result:
        print("You are correct!")
    elif result == "EQUAL":
        print("The numbers are equal. Let's try again!")
    else:
        print("You are wrong. Sorry!")

## Call the function to ask the player to input a response
player_answer = inputAnswer()


## Call the randomize function and store the number into the variable second_number
second_number = randomize()

## Compare the second_number and first_number values
result = compareNumbers()
print(f"The result is: {result}")

## Compare the result and the input answer.
compareResults()

## Reset the value of the numbers
first_number = second_number
second_number = 0

print ("## --- ## --- ## --- ##")

    

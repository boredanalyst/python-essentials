## Here are the choices

choice = {
    "rock" : "ROCK",
    "paper" : "PAPER",
    "scissors" : "SCISSORS"
}

print("CHOICES")
for key in choice.keys():
    print(key)


## THIS IS THE CODE BLOCK THAT CONFIRMS THE CHOICE OF PEOPLE.

playerChoice = ""

while playerChoice == "":

    playerChoice = input("Please choose your choice from above: ")
    playerChoice = playerChoice.lower()

    if playerChoice in choice.keys():
        print(f'You chose {choice.get(playerChoice)}!')
        continue
    else:
        print("Can you try that again?")
        playerChoice = ""

## THIS IS THE CODE BLOCK FOR FINDING THE CHOICES OF THE OPPONENT.

import random as rand

rng = (rand.randint(1,3)) - 1

oppChoices = ["rock","paper","scissor"]
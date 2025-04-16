## Loop through a list and stop if the next word ends with a letter 's'

colors = ["red","orange","yellows","greens"]

for x in colors:
    lastLetter = x[len(x)-1]
    if lastLetter == "s":
        print(f'{x}: This color ends with the letter "s"')
        break
    else:
        print(f'{x}: This color does not end with the letter "s"')

    
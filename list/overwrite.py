print("You can overwrite the values of a list.")

colors = ["red","orange","yellow"]

newColor = "violet"

print(colors)

if newColor not in colors:
    colors[0] = newColor
    print("The values have been changed.")
    print(colors)
else:
    print("Violet is already in the list.")
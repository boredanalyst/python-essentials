print("How to clear out a list.")

colors = ["red","orange","yellow"]

print(colors)

for color in colors:
    print(color)
    if len(color) >=5:
        colors.clear()

print(colors)
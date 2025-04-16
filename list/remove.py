colors = ["red","orange","yellow","green","blue","purple"]
long_colors = []

print("DELETE ANY COLOR WITH AT LEAST FIVE LETTERS")

for color in colors:
    if len(color) >= 5:
        long_colors.append(color)
        colors.remove(color)

print("These are the remaining colors")
print(colors)

print("These are the new color list with longer words.")
print(long_colors)



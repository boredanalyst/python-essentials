print("ADD AN ITEM TO A LIST")

colors = ["red","orange","yellow"]

if "violet" not in colors:
    colors.append("violet")
    print("Violet has been added to the list.")
else:
    print("Violet is already in the list.")

print(colors)
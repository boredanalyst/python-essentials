print("INSERT adds an element to the list but not at the end just like APPEND does.")

colors = ["red","orange","yellow"]

print(colors)

print("----")

if "violet" not in colors:
    halfway = round(len(colors)/2)
    colors.insert(halfway,"violet")
    print("violet has been added to the list.")
else:
    print("Violet is already in the list.")

print(colors)
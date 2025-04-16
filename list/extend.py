colors = ["red","orange","yellow"]
colors2 = ["green","blue","purple"]

print(colors)
print(colors2)

if len(colors) == 3:
    colors.extend(colors2)
else:
    print(f'The colors list has {len(colors)} elements')

print(colors)
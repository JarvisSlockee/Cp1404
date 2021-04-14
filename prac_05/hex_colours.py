COLOURS = {"aliceblue": "#f0f8ff", "cadetblue1": "#98f5ff", "darkseagreen3": "#9bcd9b", "goldenrod2": "#eeb422",
           "gray31": "#4f4f4f", "hotpink1": "#ff6eb4", "indianred1": "#ff6a6a", "lightslateblue": "#8470ff",
           "mediumorchid1": "#e066ff", "thistle2": "#eed2ee"}

for i, j in COLOURS.items():
    print("Colour options are: {}".format(i))

colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in COLOURS:
        print(colour, "hex code is", COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ").lower()

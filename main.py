from note import Note
from majorScale import MajorScale
from minorScale import MinorScale
print("Hi welcome to my app.\n")
note = None
scale = None
while(True):
    # if no scale is chosen
    if scale is None:
        # choose a note
        if note is None:
            note = input("Choose a note: ")
        menu = ("1. {0} major scale\n"
            "2. {0} minor scale\n"
            "3. Choose another note\n"
            "4. Exit").format(note)
        print(menu)
        
        # choose major or minor
        optn = input("\nChoose an option: ")
        if optn == "1":
            scale = MajorScale(note)
        elif optn == "2":
            scale = MinorScale(note)
        elif optn == "3":
            note = None
        elif optn == "4":
            break
        else:
            print("Invalid option. Try again.\n")
    # major scale
    if isinstance(scale, MajorScale):
        print(scale)
        menu = ("1. Get parallel minor\n"
            "2. Get relative minor\n"
            "3. Choose another note\n"
            "4. Exit").format(note)
        print(menu)
        optn = input("\nChoose an option: ")
        if optn == "1":
            scale = MinorScale(scale,1)
        elif optn == "2":
            scale = MinorScale(scale,2)
        elif optn == "3":
            note = None
            scale = None
        elif optn == "4":
            break
        else:
            print("Invalid option. Try again.\n")
    # minor scale
    if isinstance(scale, MinorScale):
        print(scale)
        menu = ("1. Get parallel major\n"
            "2. Get relative major\n"
            "3. Choose another note\n"
            "4. Exit").format(note)
        print(menu)
        optn = input("\nChoose an option: ")
        if optn == "1":
            scale = MajorScale(scale,1)
        elif optn == "2":
            scale = MajorScale(scale,2)
        elif optn == "3":
            note = None
            scale = None
        elif optn == "4":
            break
        else:
            print("Invalid option. Try again.\n")
print("Bye!")

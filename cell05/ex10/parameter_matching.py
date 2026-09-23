import sys

if len(sys.argv) == 2:
    para = sys.argv[1]

    txt = input("What was the parameter? ")
    if txt == para:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
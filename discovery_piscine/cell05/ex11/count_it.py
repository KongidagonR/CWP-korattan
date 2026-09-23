import sys

if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameter: {len(sys.argv) - 1}")

    for para in sys.argv[1:]:
        print(f"{para}: {len(para)}")
    

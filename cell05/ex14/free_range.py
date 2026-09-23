import sys

if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    num_list = list(range(a, b+1))
    print(num_list)

else:
    print("none")
  
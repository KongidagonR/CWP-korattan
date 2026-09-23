n = int(input("Enter Number: "))
i = 0
while i <= n:
    print("Table de", i, ":", end=" ")

    j = 0
    while j <= 10:
        print(i * j, end=" ")
        j += 1

    print()
    i += 1
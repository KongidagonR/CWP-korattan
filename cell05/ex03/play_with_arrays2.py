arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(arr)

new_arr = []

for i in range(len(arr)):
    arr[i] += 2

    if arr[i] > 5:
        if arr[i] not in new_arr:
            new_arr.append(arr[i])

print(new_arr)
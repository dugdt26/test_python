print("nhập vào 2 số:")
user_input = input()
rows = int(user_input[0])
cols = int(user_input[1])

arr = []
for x in range(rows):
    row = []
    for y in range(cols):
        row.append(x * y)
    arr.append(row)

print(arr)
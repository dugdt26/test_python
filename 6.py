count = 0
for num in range(10000,99999):
    prime = True
    for i in range(2,num):
        if (num % i ==0):
            prime = False
    if prime:
        count = count + 1
print(count)

def phanTichSoNguyen(n):
    i = 2
    listNumbers = []
    while (n > 1):
        if (n % i == 0):
            n = int(n / i)
            listNumbers.append(i)
        else:
            i = i + 1

    if (len(listNumbers) == 0):
        listNumbers.append(n)
    
    size = len(listNumbers)
    snt = ""
    for i in range(0, size - 1):
        snt = snt + str(listNumbers[i]) + " x "
    snt = snt + str(listNumbers[size-1])

    print(snt)






def main():
    
    print("Nhập số nguyên dương n =")
    n = int(input())
    phanTichSoNguyen(n)


if __name__ == "__main__":
    main()
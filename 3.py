print("Nhập 1 chuỗi:")
string_input = input()
count1 = 0
count2 = 0
for i in string_input:
    if(i.isdigit()):
        count1 = count1+1
    else:
        count2=count2+1

print("Số lượng số trong chuỗi là:")
print(count1)
print("Số lượng ký tự không phải số là:")
print(count2)

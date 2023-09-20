lst = list()
for i in range(10):
    num = int(input("Enter a number: "))
    lst.append(num)
lst.sort()
print(f"The largest number is: {lst[-1]}")
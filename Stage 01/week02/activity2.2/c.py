num = []

x= int(input("Enter number (-999 to stop): "))
while x != -999:
    num.append(x)
    x= int(input("Enter number (-999 to stop): "))

tot = sum(num)

print ("\nSum: ", tot)

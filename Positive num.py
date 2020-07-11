numlist = []

num = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, num + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    numlist.append(value)

print("\nPositive Numbers in this List are : ")
for j in range(num):
    if(numlist[j] >= 0):
        print(numlist[j], end = '   ')

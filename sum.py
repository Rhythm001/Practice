add = 0
n = int(input("Enter the number here: "))
for i in range(n):
    x = 1/(i+1)**2
    add = add + x
print(add)

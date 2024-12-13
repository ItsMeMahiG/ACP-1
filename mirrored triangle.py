print("mirrored triangle out of asterisks")
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for m in range(i):
        print("*", end="")

    print() 
def count_digits(nums):
    count = 0
    while nums > 0:
        nums //= 10
        count += 1
    return count
num = int(input("Enter a number: "))
digits = count_digits(num)
print("The number of digits in", num, "is", digits)
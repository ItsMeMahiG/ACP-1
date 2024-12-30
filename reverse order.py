def count_digits(number):
   
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count
num = int(input("Enter an integer: "))
num_digits = count_digits(num)
print("The number of digits in", num, "is", num_digits)
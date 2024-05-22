def is_armstrong_no(n):
    digits = str(n)
    ndigits = len(digits)
    #calculate sum of powers of digits
    sum_of_pow = sum(int(digit)**ndigits for digit in digits)
    #if sum of powers of digits equalent to number then return true
    return sum_of_pow == n

n = int(input("Enter a number: "))
if is_armstrong_no(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")


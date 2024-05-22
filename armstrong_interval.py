def is_armstrong_no(n):
    digits = str(n)
    ndigits = len(digits)
    #calculate sum of powers of digits
    sum_of_pow = sum(int(digit)**ndigits for digit in digits)
    #if sum of powers of digits equalent to number then return true
    return sum_of_pow == n

def find_armstrong(start, end):
    armstrong_no = []
    for n in range(start, end+1):
        if is_armstrong_no(n):
            armstrong_no.append(n)
    return armstrong_no

start = int(input("Enter the start of the interval:"))
end = int(input("Enter the end of the interval:"))

armstrong_no = find_armstrong(start, end)
if armstrong_no:
    print(f"Armstrong numbers between {start} and {end} are : {armstrong_no}")
else :
    print(f"There are no armstrong numbers between {start} and {end}.")


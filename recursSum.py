def recur(n):
    if n == 0:
        return 0
    else:
        return n + recur(n - 1)

sum = recur(10)
print(f"The sum of numbers from 0 to 10 is: {sum}")

    

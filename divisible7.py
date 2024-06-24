def divi7():
    count = 0
    sum = 0
    for num in range(101, 200):
        if num % 7 == 0:
            count += 1
            sum += num
    
    return count, sum

divi_count, divi_sum = divi7()

print(f"No.of integers divisible by 7: {divi_count}")
print(f"Sum of these integers: {divi_sum}")

def multiplication_table(n,limit):
    for i in range(1,limit+1):
        print(str(n)+" x "+str(i)+" = "+str(n*i))
x = int(input("Enter the number for multiplication table: "))
limit = int(input("Enter the limit for table: "))
print("Multiplication table for "+str(x)+" : ")
multiplication_table(x,limit)
def fib(n):
    fib_seq = [0,1]
    for i in range(2,n):
        nxt = fib_seq[-1]+fib_seq[-2]
        fib_seq.append(nxt)
    return fib_seq
x = int(input("No.of terms in series: "))
fib_seq = fib(x)
print("Fibonacci sequence upto "+str(x)+" : ")
print(fib_seq)

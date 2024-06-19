start = int(21/2)
end = int(21/2 - 1)
for i in range(1,11):
    for j in range (1,21):
        if j in range(start,end):
            print("*",end="")
        else : print(" ",end = "")
    start-=1
    end +=1
    print()
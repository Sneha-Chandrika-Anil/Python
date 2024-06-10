names = ["Urmila","Gracen","Varghese","Sreekesh","Sreekumar"]
#if-else condition,for loop, while loop
# on the margin - global scope
#indentation should be uniform in that particular block/scope
if "Gracen" in names:
    print("Gracen is in the list")
else:
    print("Gracen is not in the list")
names.sort()

for x in names:
    print(x)

i = 0
while i < len(names):
    print(names[i])
    i+=1

#armstrong number

num= int(input("enter a number:"))
temp = num
sum = 0
digits=len(str(num))

while temp>0 :
    digit = temp % 10
    sum = sum + (digit**digits)
    temp = temp//10

if (sum == num ):
    print("number is armstrong")
else :
     print("number is not armstorng")

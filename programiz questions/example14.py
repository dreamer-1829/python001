num=int(input("enter the number: "))
flag= False
if num ==0 or num == 1:
    flag= True
else:
    for i in range(2,num):
        if num % i==0:
            flag=True
            break
if flag:
    print("the number is not prime")
else:
    print("the number is prime")
    
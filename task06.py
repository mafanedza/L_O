num1 = int(input(5))
num2 = int(input(9))
num3 = int(input(4))

if (num1 >= num2):
    if(num1 >= num3):
       print( " num1 is the largest")
    else:
        print("num3 is the largest")
elif  (num2 >= num3):
    print("num2 is the largest")

else:
    print("num3 is the largest")
n=int(input("Enter a number:"))

if n<=100:
    print("You are alive:")
    if n%2==0:
        print("The value is even")
    else:
        print("The value is odd")
     
elif n>=101 and n<500:
    print("You are died:")
    if n%2==0:
        print("The value is even")
    else:
        print("The value is odd")

else:
    print("You are not a human beaing:")
    if n%2==0:
        print("The value is even")
    else:
        print("The value is odd")

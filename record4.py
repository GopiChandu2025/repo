start=int(input("Enter starting value:"))
end=int(input("Enter end value:"))

print(f"Prime values between {start} and {end}:")


for i in range(1,end+1):
    if i>1:
        for n in range(2,i):
            if i%2==0:
                break
        else:
            print(i)
   

    

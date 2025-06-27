def factorial(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result
    
while True:
    n=int(input("Enter any number:"))
    if n<0:
        print("You must Grater then 0")
    elif n==0:
        print("Factorial of '0' is 1")
    else:
        print(f"Factorial of {'n'} is :{factorial(n)}")
    

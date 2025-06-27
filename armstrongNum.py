
n = int(input("Enter any number :"))
a = n
sum = 0
l = len(str(n))

while n > 0:
    digit = n % 10
    sum = sum+(digit ** l)
    n = n//10

if sum == a:
    print("number is an Armstrong number.")
else:
    print("number is not an Armstrong number.")

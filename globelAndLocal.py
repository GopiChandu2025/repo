a=10
def hello():
    a=20
    print("local a in inner:",a)

print("Globel a in outer",a)
hello()
print("Globel a in outer",a)



print("----------------------------")

a=10
def hello():
    global a
    a=20
    print("local a in inner:",a)

print("Globel a in outer",a)
hello()
print("Globel a in outer",a)


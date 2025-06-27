string=input("Enter a word:")
string=string.casefold()   #case fold is used to consider the capital and small lettars as same
reverse_string=reversed(string)
if list(string) == list(reverse_string):  
    print("It is a pallidrome")
else:
    print("It isn't a pallidrome")    

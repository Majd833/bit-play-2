def ifsame(number1,number2):
    if ((number1^number2)!=0):
        print("These numbers aren't equal")
    else:
        print("the numbers are equal")
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
ifsame(number1,number2)
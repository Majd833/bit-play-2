def revbits(number):
    rev=0
    while (number>0):
        rev=rev<<1
        if (number & 1==1):
            rev=rev^1
        number=number>>1
    return rev
number=int(input("Enter the numberto reverse:"))
print("the number with the reversed bits:",revbits(number))
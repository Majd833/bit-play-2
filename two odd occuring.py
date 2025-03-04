def twoodd(arr,size):
    xor2=arr[0]
    x=0
    y=0
    set=0
    for i in range (1,size):
        xor2=xor2^arr[i]
    set=xor2 & ~(xor2-1)
    for i in range(size):
        if (arr[i]&set):
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("the two ODD elements are ",x,"&",y)
arr=[]
arrsize=int(input("Enter size of the array:"))
for i in range (0,arrsize):
    z=int(input("Enter element:"))
    arr.append(z)
twoodd(arr,arrsize)
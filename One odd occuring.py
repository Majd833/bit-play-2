def oddoccuring(arr):
    res=0
    for element in arr:
        res=res^element
    return res
arr=[]
n=int(input("Enter the array size:"))
while(n):
    num=int(input("Enter number:"))
    arr.append(num)
    n-=1
print("The odd occuring number is:", oddoccuring(arr))
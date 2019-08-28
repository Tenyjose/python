from array import *
p=0
def search(a,n,s):
    global p
    start=0
    stop=n-1
    while start<stop:
        mid=(start+stop)//2
        p=mid
        if a[mid]==s:
            return True
        else:
            if a[mid]>n:
                stop=mid-1
            else:
                start=mid+1
    return False
a=array("i",[])
n=int(input("Enter the number of elements in the array :: "))
for i in range(n):
    x=int(input(f"Enter the array element {i}:: "))
    a.append(x)
print(a)
s=int(input("Enter the number to be searched :: "))



if search(a,n,s)=True:
    print("FOUND @ ",p+1,"position")
else:
   print("NOT FOUND :( ")

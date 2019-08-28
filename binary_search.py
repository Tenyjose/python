from array import *
p=0
def search(nums,n):
    global p
    start=0
    stop=len(nums)
    while start<stop:
        mid=(start+stop)//2
        p=mid
        if nums[mid]==n:
            return True
        else:
            if nums[mid]>n:
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



if search(a,n):
    print("FOUND @ ",p+1,"position")
else:
   print("NOT FOUND :( ")

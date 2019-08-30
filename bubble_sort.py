def sort(a):
    for i in range(0,len(a),1):   #REFFER THE POSITION SO START,STOP AND STEP VALUES SHOULD BE SPECIFIED !
        for j in range(0,len(a)-1,1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=list()
n=int(input("Enter the number of elements to be included in list :: "))
for i in range(n):
    b=int(input("Enter the list element :: "))
    a.append(b)

sort(a)
print(a)

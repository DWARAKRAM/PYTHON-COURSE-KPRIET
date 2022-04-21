a=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS : "))
for i in range(0,n):
    b=int(input())
    a.append(b)
print("THE LIST IS : ",a)
a_copy=a[:]
a_copy.sort()
if a_copy==a:
    print("THE LIST IS IN ASCENDING ORDER")
else :
    print("THE LIST IS NOT IN ASCENDING ORDER")

a = []
n = int(input("ENTER THE NUMBER OF ELEMENTS: "))
for i in range (0,n):
    print("ENTER THE VALUE: ")
    b = str(input())
    a.append(b)
c=tuple(a)
print("THE TUPLE IS: ",c)
d=''
for j in c:
    d=d+j
print("THE STRING IS: ",d)

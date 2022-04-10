print("****NOTE:STRING 1 IS LARGER THAN STRING 2****")
S1= input("Enter the string 1 : ").lower()
S2= input("Enter the string 2 : ").lower()
count=0
l=[]
for i in S2:
    if i not in l:
        l.append(i)
for character1 in S1:
    for character2 in S2:
        if character1 == character2:
            count += 1
if count >= len(l):
    print("YES")
else:
    print("NO")

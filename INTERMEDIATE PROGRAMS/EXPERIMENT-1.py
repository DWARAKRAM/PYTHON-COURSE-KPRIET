integer = int(input("Enter the integer :"))
n = integer
if(n%2==0):
    rev=0
    while(n!=0):
        dig=n%10
        n=n//10
        rev=rev*10+dig
    if(rev==integer):
        print("The given number is even and a Palindrome")
    else:
        print("The given number is even but not a Palindrome")
else:
    i=1
    f=1
    while(i<=n):
        f=f*i
        i+=1
    print("The factorial of the number is : ",f)
    fact=f
    count=0
    while(fact!=0):
        fact= fact//10
        count= count+1
    print("The number of digits in the factorial is : ",count)
    print("The given number is Odd")

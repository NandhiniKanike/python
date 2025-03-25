n=int(input("ENTER THE NUMBER :"))
a,b=0,1
print(a)
print(b)
i=0
while i<n:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1
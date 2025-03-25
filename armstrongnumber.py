n=int(input("ENTER THE NUMBER :"))
org=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if org==sum:
    print(f"GIVEN {org} IS A ARMSTRONG NUMBER ")
else:
    print(f"GIVEN {org} IS NOT A ARMSTRONG NUMBER ")

n=int(input("ENTER THE NUMBER :"))
esum=0
osum=0
for i in range(n+1):
    if i%2==0:
        esum+=i
    else:
        osum+=i
print("SUM OF EVEN NUMBERS ARE :",esum)
print("SUM OF ODD NUMBERS ARE :",osum)

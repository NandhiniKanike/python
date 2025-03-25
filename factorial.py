def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("ENTER THE NUMBER TO FIND THE FACTORIAL :"))
result=fact(n)
print(f"FACTORIAL OF {n} NUMBER IS :",fact(n))
    
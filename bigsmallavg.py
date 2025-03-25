n1=int(input("ENTER THE FIRST NUMBER :"))
n2=int(input("ENTER THE SECOND NUMBER :"))
n3=int(input("ENTER THE THIRD NUMBER :"))
def largest(n1,n2,n3):
    if (n1>n2 and n1>n3):
     print(f"FIRST NUMBER {n1} IS LARGEST")
    elif (n2>n1 and n2>n3):
     print(f"GIVEN SECOND NUMBER {n2} IS LAREGEST ")
    else:
     print(f"GIVEN THIRD NUMBER {n3} IS LARGEST ")
largest(n1,n2,n3)
def smallest(n1,n2,n3):
     if (n1<n2 and n1<n3):
      print(f"FIRST NUMBER {n1} IS SMALLEST")
     elif (n2<n1 and n2<n3):
      print(f"GIVEN SECOND NUMBER {n2} IS SMALLEST ")
     else:
      print(f"GIVEN THIRD NUMBER {n3} IS SMALLEST")
smallest(n1,n2,n3)
tot=n1+n2+n3
print("TOTAL =",tot)
avg=int(tot/3)
print("AVERAGE OF THREE NUMBERS = ", avg)

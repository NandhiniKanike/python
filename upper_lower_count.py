str=input("ENTER A STRING WITH THE COMBINATION OF UPPER AND LOWER CASE :")
upper=0
lower=0
for i in range(len(str)):
    if str[i].isupper():
        upper+=1
    else:
        lower+=1
print("COUNT OF UPPER CASE IN GIVEN STRING :",upper)
print("COUNT OF LOWER CASE IN GIVEN STRING :",lower)
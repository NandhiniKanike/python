str=input("ENTER A STRING:")
result=""
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(str)):
    if str[i] not in vowels:
        result=result+str[i]
print("AFTER REMOVING VOWELS IN GIVEN STRING :",result)
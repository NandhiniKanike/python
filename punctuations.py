def remove_punctuations(str):
    result=" "
    for char in string:
        if char!=',' and char!='.' and char!='!':
             result += char
    return result
string=input("ENTER A STRING WITH PUNCTUATIONS :")
print(remove_punctuations(string))

#positional arguments
def display(name,age):
    r=name
    s=age
    print("NAME :",r)
    print("AGE:",s)
display('nandhini',20)
display(18,'vyshanavi')
#keyword arguments
def display(name,age):
    r=name
    s=age
    print("NAME :",r)
    print("AGE:",s)
display(name='nandhini',age=20)
display(age=18,name='vyshanavi')
#default arguments
def display(name,age,school='ABCD'):
    r=name
    s=age
    d=school
    print("NAME :",r)
    print("AGE:",s)
    print("SCHOOL NAME :",d)
display(name='nandhini',age=20)
display(age=18,name='vyshanavi',school='MSEMHS')
#variable length arguments
def readnames(*names):
    for i in names:
        print(i)
readnames('nandhini','vyshnavi')
readnames("soujanya",'nerraja','anil','sunil')

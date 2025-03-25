#tuple creation
t1=()
t2=(1,2,3,4,5)
t3=(1,2.3,'nandhu',False)
print(t1)
print(t2)
print(t3)
#accessing tuples
t4=(1,2,3,4,5,6)
print(t4[3])
print(t4[1:5])
print(t4[1::2])
print(t4[::-1])
#apply operators
t5=(0,1,2,3,4,5)
t6=('a','b','c','d')
t7=t5+t6
print(t7)
print(t5==t6)
#usage of methods
t8=(3,5,6,2,78,7)
t8.index(5)
print(t8)
print(min(t8))
print(max(t8))
print(sorted(t8))
print(len(t8))
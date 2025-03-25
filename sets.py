#set creation
s={}
s1={1,2,3,4,5}
print(s)
print(s1)
#accessing elements
s2={1,2,3,4,5,6}
for i in s2:
    print(i)
#apply operators
s3={1,2,3,4,6}
s4={1,2,0,4}
if 1 in s3:
    print(True)
print(s3&s4)
print(s3|s4)
print(s3^s4)
print(not s3)
#usage of methods
s5=set()
s5.add(5)
print(s5)
s6={1,2,3,4,5,6,7,8}
s6.clear()
print(s6)
s7=s5.copy()
print(s7)
s8={1,2,3,4,5,6,7,8}
s8.remove(5)
print(s8)
s8.pop()
print(s8)
s8.discard(6)
print(s8)
s9={1,2,3,4,5}
print(s8.intersection(s9))
print(s8.union(s9))
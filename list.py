#list creation
l1=[]
l2=[1,2,3,4,5]
l3=[1,1.2,'nandhini',True]
print(l1)
print(l2)
print(l3)
#accessing elements
print(l2[0])
print(l2[1:4])
print(l3[0:])
print(l2[::-1])
#apply operators
l4=[1,2,3,4]
l5=[5,6,7,8]
print(l4+l5)
print(l4==l5)
print(l4<l5)
print(l4>l5)
print(l4 and l5)
print(l4 or l5)
print(not l5)
#usage of methods
l6=[1,2,3,4,5,6]
l6.append(10)
print(l6)
l7=l6.copy()
print(l7)
print(l6.pop())
l6.remove(5)
print(l6)
l6.reverse()
print(l6)
print(min(l6))
print(max(l6))
l8=[11,22,33,44,55]
l8.extend(l6)
print(l8)
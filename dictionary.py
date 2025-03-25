d={}
d1={
    1:'nandhu',2:"soujanya"
}
print(d1)
print(d)
#accessing elements
d2={
    1:'sunil',2:'rajesh',3:'mahesh',4:'siraj'
}
print(d2.keys())
print(d2.values())
print(d2.get(2))
print(3 in d2)
for i in d2.keys():
    print(i)
for i in d2.values():
    print(i)
#apply opeartors
d3={
    1:'a',2:'b',3:'c'
}
d4={
    4:'c',5:'b',6:'c'
}
print(d3==d4)
print(d3!=d4)
print(d3 and d4)    
print(d3 or d4)
print(not d3)
#usage of diiferent methods
d5={
    1:'one',2:'two'
}
d5.clear()
print(d5)
d6={
    1:'priya',2:'pavani',3:'gopi'
}
c=d6.copy()
print(c)
d7={
    1:'banana',2:'carrot',3:'344',4:'guva'
}
d7.pop(3)
print(d7)
d8={
    1:'banana',2:'carrot',3:'grapes',4:'guva'

}
d8.popitem()
print(d8)
d9={
    1:'cse',2:'eee',3:'ece',4:'mec'

}

d9.update({5:'mca'})
print(d9)
print(d7.keys())
print(d7.values())


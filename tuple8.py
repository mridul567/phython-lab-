#Coloning of tuple
t=(1,2,3.5,[])
d=eval(str(t))
d[-1].append(100)
print(t)
print(d)


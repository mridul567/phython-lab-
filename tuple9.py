#Repeating items of tuple
t=(1,2,3,4,1,1.5)
print(t)
for i in t:
	if t.count(i)>1:
		print(i)
		break

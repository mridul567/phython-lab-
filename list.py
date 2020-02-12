l=[]
d=[]
print("enter the list")
l=list(map(int , input().split()))
b=[]
for i in l:
	if l.count(i)==2:
		l.remove(i)
	else:
		b.append(i)
	print(i,end="*")


#intersection of two lists
print("enter the 1st list")
l1=[]
l1=list(map(int,input().split()))
print("enter the 2nd list")
l2=list(map(int,input().split()))
l3=[i for i in l1 if i in l2]
print("intersection of list:")
print(l3)
l4=l1+l2+l3
l4=[i for i in l4 if l4.count(i)==1]
print("union of lists:")
print(l4)

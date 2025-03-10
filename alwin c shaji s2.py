n=int(input("enter size of array"))
a=[]
for i in range(n):
    g=int(input("enter numbers one by one: "))
    a.append(g)
z=1
while(1):
    if z in a:
        z+=1
    else:
        print("the smallest number not present in the array is ",z)
        break
        



list1=[int(x) for x in input().split()]

limit=len(list1)

i=0;leaders=[];flag=0
while i<limit-1:
    first=list1[i]
    for k in range(i+1,limit-1):
        if list1[k]>first:
            break
    else:
        flag=1
    
    if flag==1:
        leaders.append(first)
    i=i+1

        

leaders.append(list1[limit-1])
print(leaders)
a=[2,3,4,5]
i=0
for i in a:

    j=i+1
    for j in a:
        print("I'm in")
        print(a[j])
        print(a[i])
        j+=1
        if j>len(a)-1:
            break
    if i>len(a)-1:break

i+=1

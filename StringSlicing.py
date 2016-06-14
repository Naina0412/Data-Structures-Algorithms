

a="NainaVinay"
for i in range(len(a)):
    print (i)
    #print(a[:i])
    #print(a[:-1])
    #print(a[i+1:])
    #print("Peep")
    print(a[:-3])
    print(a[-1::])
    print("-1 saga",a[::-1])
    word=a[:i]+'_'+a[i+1:]
    print(word)
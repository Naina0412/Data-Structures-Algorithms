
hashItem=[]
hashItemList=[54,32,17,88,45]
hashItemsList=['c','d','a']
#c=(hashItemList)
hashItemsOrd=0
no= 11

for i in range(len(hashItemList)):
    hashItemsOrd+=ord(hashItemsList[i])
    print(hashItemsOrd)
    calculatedHash=hashItemList[i]%no
    print(calculatedHash)
    hashItem.append(calculatedHash)
print(hashItem)


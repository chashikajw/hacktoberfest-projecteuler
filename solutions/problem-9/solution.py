def storeSqareValues(limitNum):
    sqrevalus = []
    val = 1
    i = 1
    while(val < limitNum-5): #minimum two valuse shuold be 1 and 2(1^2+2^2=5)
        sqrevalus.append(val)
        i += 1
        val = i*i       
        
    return sqrevalus

def findsqares(limitNum):
    sqareValues = storeSqareValues(limitNum)
    lengtharr = len(sqareValues)
    for i in range(lengtharr-1,1,-1):
        for j in range(lengtharr):
            for k in range(1,lengtharr):
                total = sqareValues[i] + sqareValues[j] + sqareValues[k]
                if(total == limitNum):
                    print("value 1: "+str(sqareValues[k]))
                    print("value 2: "+str(sqareValues[j]))
                    print("value 3: "+str(sqareValues[i]))
                    return (sqareValues[i]*sqareValues[j]*sqareValues)
                elif(total < limitNum):
                    continue
                else:
                    break

    
        
print("product of values are: " + str(findsqares(1000)))

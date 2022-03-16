Arr = []
S = " "

konec = 0

while S != "=":
    S = str(input())
    
    Arr.append(S)
    
for i in range(len(Arr)):
    if (Arr[i] != '-') and (Arr[i] != '=') and (Arr[i] != '+') and (Arr[i] != '-'):
        Arr[i] = int(Arr[i])

while konec != len(Arr):
    k = 0
    
    
    ohmygod = len(Arr)
    
    if Arr[konec] == '*':
        Arr[konec] = Arr[konec-2] * Arr[konec-1]
        
        Arr[konec-1] = " "
        Arr[konec-2] = " "
        
        konec = 0        

    elif Arr[konec] == '+':
        Arr[konec] = Arr[konec-2] + Arr[konec-1]
        
        Arr[konec-1] = " "
        Arr[konec-2] = " "
        
        konec = 0

    elif Arr[konec] == '-':
        Arr[konec] = Arr[konec-2] - Arr[konec-1]
        
        Arr[konec-1] = " "
        Arr[konec-2] = " "
        
        konec = 0 

    elif Arr[konec] == '=':
        print(Arr[konec-1])
        break
    
    while k < ohmygod:
        if Arr[k] == " ":
            Arr.pop(k)
        
        ohmygod = len(Arr)
        
        k+=1
    
    konec+=1

print(Arr[0])

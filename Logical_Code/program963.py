# Accespt N Element number from user and find Minimun number

def Minimun(Brr):
    iMin = Brr[0]
    
    for i in range(len(Brr)):
        if(Brr[i] < iMin):
            iMin = Brr[i]
        
    return iMin
        
def main():
    Size = 0
    Arr = []
    
    print("Enter Number of Elements : ")
    Size = int(input())
    
    print("Enter the Elements : ")
    
    Value = 0
    
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)
        
    Ret = Minimun(Arr)
    
    print("Minimun is : ",Ret)    
        
    
main()      
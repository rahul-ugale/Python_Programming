# Accespt String from user and Count Small digits
def CountSmall(Brr):
    iCount = 0
    
    for i in range(len(Brr)):
        if(Brr[i] >= 'a' and Brr[i] <= 'z'):
            iCount = iCount + 1
            
    return iCount            

def main():
    print("Enter String : ")
    Arr = input()
    
    Ret = CountSmall(Arr)
    
    print("Number of Small Characters are : ",Ret)
    
main()      
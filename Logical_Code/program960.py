# Accespt N Element number from user
    
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
        
    print(Arr)    
        
    
main()      
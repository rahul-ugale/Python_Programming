# Accespt String from user and conver to string Togale case 

def TogaleCase(Brr):
    Result = ""
    for ch in Brr:
        if(ch >= 'A' and ch <= 'Z'):
            Result = Result + chr(ord(ch) + 32)
        else:
            Result = Result + chr(ord(ch) - 32)
              
    return Result

def main():
    print("Enter String : ")
    Arr = input()
    
    Ret = TogaleCase(Arr)
    
    print("Updated String is : ",Ret)
    
main()      
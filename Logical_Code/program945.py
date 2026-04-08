# Check EvenOdd Number

def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even Number")
    else:
        print("It is Odd Number")    

def main():
    Value = 0
    
    print("Enter Number : ")
    Value = int(input())
    
    CheckEven(Value)
    
main()      
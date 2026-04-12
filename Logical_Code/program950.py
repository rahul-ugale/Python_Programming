# Display of Digits
def DisplayDigits(No): 
    
    Digit = 0 
    while(No != 0):
        Digit = No % 10
        print(Digit)
        No = No / 10  # Error
             
def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    DisplayDigits(Value)
                
main()      
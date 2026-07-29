# Singly Linear Linked List
# Done
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class SinglyLL:
    # Done
    def __init__(self):
        self.first = None 
        self.iCount = 0 
    
     # Done   
    def InsertFirst(self,no):
        newn = Node(no)
        
        # LL is Empty
        if(self.first == None):
            self.first = newn
        # It contains at list one Node    
        else:
            newn.next = self.first
            self.first = newn
        
        self.iCount = self.iCount + 1        
    
    # Done
    def InsertLast(self,no):
        newn = Node(no)
        
        # LL is Empty
        if(self.first == None):
            self.first = newn
        # It contains at list one Node    
        else:
            temp = self.first
            
            while(temp.next != None):
                temp = temp.next
                
            temp.next = newn    
        
        self.iCount = self.iCount + 1  
    
    # Done
    def InsertAtPos(self,no,pos):
        # Invalid Position Filter
        if(pos < 1 or pos > (self.iCount + 1)):
            print("Invalid Position")
            return
        
        if(pos == 1):
            self.InsertFirst(no)
            return
        elif(pos == self.iCount + 1):
            self.InsertLast(no)
            return
        else:
            newn = Node(no)
            temp = self.first
            
            for i in range(1,pos - 1):
                temp = temp.next
                
            newn.next = temp.next
            temp.next = newn
            
            self.iCount = self.iCount + 1    
    # Done
    def DeleteFirst(self):
        
        if(self.first == None):
            return
        
        temp = self.first
        
        self.first = self.first.next
        
        del temp
        
        self.iCount = self.iCount - 1
        
    # Done
    def DeleteLast(self):
        # LL is Empty 
        if(self.first == None):
            return
        
        # LL contains one Node
        if(self.first.next == None):
            del self.first
            self.first = None
            self.iCount = 0
            
        # LL contains more than 1    
        else:      
            temp = self.first
            
            while(temp.next.next != None):
                temp = temp.next
                
            del temp.next
            temp.next = None    
        
            self.iCount = self.iCount - 1
    
    def DeleteAtPos(self,pos):
        pass
    
    # Done
    def Display(self):
        temp = self.first
        
        while(temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next 
         
        print("None")      
    
    # Done
    def Count(self):
        return self.iCount     
        
def main():
    sobj = SinglyLL()
    
    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
    
    sobj.InsertLast(111)
    sobj.InsertLast(121)
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
    
    sobj.InsertAtPos(75,4)
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
    
    sobj.DeleteFirst()
    sobj.DeleteFirst()
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
    
    sobj.DeleteLast()   
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())     
    
if __name__ == "__main__":
    main()
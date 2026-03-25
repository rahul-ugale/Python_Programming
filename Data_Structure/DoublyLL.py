################################################################################
## 
##   Structure Name : Node
##   Description    : Represents a node of Doubly Circular Linked List
##   Members        :
##       first  - Stores value of type Value
##       next   - Pointer to next node
##       prev  - Pointer to previous node
##
################################################################################

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None
 
################################################################################
## 
##   Class Name   : DoublyCLL
##   Description  : Implements Doubly Circular Linked List operations.                
##   Author       : Rahul Balasaheb Ugale
##   Date         : 22/03/2026
##
################################################################################
       
class DoublyLL:
    
    ############################################################################
    ## 
    ##   Constructor Name   : __init__
    ##   Description        : Initializes an empty doubly circular linked list.                
    ##   Author             : Rahul Balasaheb Ugale
    ##   Date               : 22/03/2026
    ##
    ############################################################################
    def __init__(self):
        self.first = None 
        self.last = None
        self.iCount = 0 
    
    ############################################################################
    ## 
    ##   Function Name :  InsertFirst
    ##   Input         :  Data of node
    ##   Description   :  Used to insert node at first position.                
    ##   Author        :  Rahul Balasaheb Ugale
    ##   Date          :  22/03/2026
    ##
    ############################################################################
    def InsertFirst(self,no):
    
        newn = Node(no)
        
        # LL is Empty
        if(self.first == None):
            self.first = newn
        # It contains at list one Node    
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn
        
        self.iCount = self.iCount + 1        
    
    ############################################################################
    ## 
    ##   Function Name :  InsertLast
    ##   Input         :  Data of node
    ##   Description   :  Used to insert node at Last position.
    ##   Author        :  Rahul Balasaheb Ugale
    ##   Date          :  21/03/2026
    ##
    ############################################################################
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
            temp.prev = newn    
        
        self.iCount = self.iCount + 1  
    
    ############################################################################
    ## 
    ##   Function Name :  InsertAtPos
    ##   Input         :  Data of node
    ##   Description   :  Used to insert node at position.                
    ##   Author        :  Rahul Balasaheb Ugale
    ##   Date          :  21/03/2026
    ##
    ############################################################################
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
            newn.prev = temp
                
            temp.next.prev = newn 
            temp.next = newn
            
            self.iCount = self.iCount + 1    
    
    ############################################################################
    ## 
    ##   Function Name :  DeleteFirst
    ##   Input         :  Data of node
    ##   Description   :  Used to Delete node at first position.                
    ##   Author        :  Rahul Balasaheb Ugale
    ##   Date          :  21/03/2026
    ##
    ############################################################################
    def DeleteFirst(self):
        
        if(self.first == None):
            return
        
        temp = self.first
        
        self.first = self.first.next
        self.first.prev = None
        
        del temp
        
        self.iCount = self.iCount - 1
        
    ############################################################################
    ## 
    ##   Function Name :  DeleteLast
    ##   Input         :  Data of node
    ##   Description   :  Used to Delete node at Last position.                
    ##   Author        :  Rahul Balasaheb Ugale
    ##   Date          :  21/03/2026
    ##
    ############################################################################
    def DeleteLast(self):
        # LL is Empty 
        if(self.first == None):
            return
        
        # LL contains one Node
        if(self.first.next == None):
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
    
    ############################################################################
    ## 
    ##   Function Name :  DeleteAtPos
    ##   Input         :  Data of node
    ##   Description   :  Used to Delete node at position.                
    ##   Author        :  Rahul Balasaheb Ugale
    ##   Date          :  21/03/2026
    ##
    ############################################################################
    def DeleteAtPos(self,pos):
        # Invalid Position Filter
        if(pos < 1 or pos > (self.iCount)):
            print("Invalid Position")
            return
        
        if(pos == 1):
            self.DeleteFirst()
            return
        elif(pos == self.iCount):
            self.DeleteLast()
            return
        else:
            temp = self.first
            
            for i in range(1,pos - 1):
                temp = temp.next
            
            temp.next = temp.next.next
            del temp.next.prev
            temp.next.prev = temp    
            
            self.iCount = self.iCount - 1
            
    ############################################################################
    ## 
    ##   Function Name :  Display
    ##   Input         :  Data of node
    ##   Description   :  Used to Display node.                
    ##   Author        :  Rahul Balasaheb Ugale
    ##   Date          :  21/03/2026
    ##
    ############################################################################
    def Display(self):
        temp = self.first
        
        if(self.first == None):
            print("Linked List is Empty")
            return
        
        print("None <=> ",end=" ")
        
        while(temp != None):
            print("| ",temp.data," |<=>",end=" ")
            temp = temp.next 
         
        print("None")      
    
    ############################################################################
    ## 
    ##   Function Name :  Count
    ##   Input         :  Data of node
    ##   Description   :  Used to Count node.                
    ##   Author        :  Rahul Balasaheb Ugale
    ##   Date          :  21/03/2026
    ##
    ############################################################################
    def Count(self):
        return self.iCount     

################################################################################
## 
##   Function Name :  main
##   Description   :  Entry point of program to test Singly Circular Linked List.                
##   Author        :  Rahul Balasaheb Ugale
##   Date          :  21/03/2026
##
################################################################################        
def main():
    sobj = DoublyLL()
    print("====================== InsertFirst ==============================")
    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
    print("====================== InsertLast ==============================")
    sobj.InsertLast(111)
    sobj.InsertLast(121)
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
    print("====================== InsertAtPos ==============================")
    sobj.InsertAtPos(75,4)
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
    print("====================== DeleteFirst ==============================")
    sobj.DeleteFirst()
    sobj.DeleteFirst()
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
    print("====================== DeleteLast ==============================")
    sobj.DeleteLast()   
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count()) 
    print("====================== DeleteAtPos ==============================")
    sobj.DeleteAtPos(3)
    
    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ",sobj.Count())
            
    
if __name__ == "__main__":
    main()
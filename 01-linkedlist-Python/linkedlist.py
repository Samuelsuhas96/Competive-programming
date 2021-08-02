"""
The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom.
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def printer(self):
        a=self.value
        b=self.next
        return a,b
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
#     def  printer(self):
#         return(self.head)

    def append(self, new_element):
        new_element.next = self.head
        self.head = new_element
        # # print(new_element.value)
        # self.head = new_element
        # print(self.head.next)
        return self.head.value
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        count = 1
        b = self.head
        while(True):
            a = b
            c = a.value
            # print(c)
            if count ==  position:
                return c
            elif b.next == None:
                return None
            count += 1
            b  = a.next
            
            # print(b.value)
        # a = b
        # print(a)
        # c = a.value
        # print(c)
        # count+=1
        # # if count ==  position:
        # #     return a 
        # b  = a.next
        # # print(b.value)
        # a = b
        # print(a.value)
        # b = a.next
        # a = b
        # print(a.value)

            
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        count = 1
        b = self.head
        while(True):
            a = b
            c = a.value
            # print(c)
            if count ==  position-1:
                new_element.next = a.next
                a.next = new_element
                return a.next.value
            elif b.next == None:
                return "Position not there in the list"
            count += 1
            b  = a.next





    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        self.head=self.head.next
        return (self.head.value)

        


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
L_l = LinkedList(e1)
L_l.append(e2)
L_l.append(e3)
# L_l.append(e4)
print(L_l.insert(e4,2))
# print(L_l.get_position(6))
# print(L_l.delete(1))
# print(L_l.get_position(1))

# print(e1.Element())
# print(e1.printer())
# print(e1.next)
# print(L_l.insert(1,3))

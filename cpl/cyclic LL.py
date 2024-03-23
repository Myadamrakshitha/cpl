class Node:
    def __init__ (self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__ (self):
        self.head=None
    def create(self,n):
        i=0
        while i<n:
            val=int(input("Enter data:"))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next != None:
                    t=t.next
                t.next=new_node
            i=i+1
    def cyclicList(self):
        i=0
        curr=self.head
        while i<100:
            print(curr.val,end="-->")
            curr=curr.next
            i+1
obj=LinkedList()
n=int(input("Enter n value"))
obj.create(n)
print("LinkedList")
obj.show(obj.head)

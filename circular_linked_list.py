class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next is not self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data)

    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head

    def insert_end(self,data):
        temp=self.head
        new_node=Node(data)
        while(temp!=self.tail):
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        self.tail=new_node

    def insert_mid(self,pos,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            if pos==1:
                insert_begin(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                new_node.next=temp.next
                temp.next=new_node
            
                
    def delete_begin(self):
        temp=self.head
        while(temp!=self.tail):
            temp=temp.next
        temp.next=self.head.next
        self.head=self.head.next

    def delete_end(self):
        temp=self.head
        while(temp!=self.tail):
            temp=temp.next
        self.tail=temp
        temp.next=self.head

    def delete_mid(self,pos):
        if self.head is None:
            print("CLL is empty")
        elif pos==1:
            delete_end()
        else:
            temp=self.head.next
            prev=self.head
            for i in range(1,pos-1):
                temp=temp.next
                prev=prev.next
            prev.next=temp.next
                #temp.next=None
cl=cll()

node_1=Node(10)
cl.head=node_1

node_2=Node(20)
node_1.next=node_2

node_3=Node(30)
node_2.next=node_3

node_4=Node(40)
node_3.next=node_4
cl.tail=node_4

cl.tail.next=cl.head

cl.display()

cl.insert_begin(50)
cl.display()

cl.insert_end(60)
cl.display()

cl.insert_mid(5,70)
cl.display()

cl.delete_begin()
cl.display()

cl.delete_end()
cl.display()

cl.delete_mid(4)
cl.display()


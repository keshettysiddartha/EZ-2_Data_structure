class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

    def insert_begin(self,data):
        new_node=Node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node

    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
        temp.next=None

    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None

    
    def delete_position(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        temp.prev=prev
        
node_1=Node("aa")
print(node_1.data)
dl=dll()
dl.head=node_1
node_2=Node("bb")
node_1.next=node_2
node_2.prev=node_1
node_3=Node("cc")
node_4=Node("dd")
node_5=Node("ee")
node_2.next=node_3
node_3.prev=node_2
node_3.next=node_4
node_4.next=node_5
node_5.next=None
dl.display()
print("")
dl.insert_begin("ff")
dl.display()
print("")
dl.insert_end("gg")
dl.display()
print("")
dl.insert_position(0,"hh")
dl.display()
print("")
dl.delete_begin()
dl.display()
print("")
dl.delete_end()
dl.display()
print("")
dl.delete_position(6)
dl.display()

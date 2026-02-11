class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_end(self,data):
        ne=Node(data)
        if self.head is None:
            self.head = ne
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def insert_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np

    def display(self):
        if self.head == None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
L=SLL()
n=Node(10)
L.head=n
n1=Node(20)
L.head.next=n1
n2=Node(30)
n1.next=n2
L.insert_begin(5)
L.insert_end(7)
L.insert_pos(4,25)
L.display()
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL():
    def __init__(self):
        self.head=None
    def arrToLL(self,arr):
        if not arr:
            return
        self.head=Node(arr[0])
        temp=self.head
        n=len(arr)
        for i in range(1,n):
            newNode=Node(arr[i])
            temp.next=newNode
            temp=temp.next
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
arr=[1,2,3,4,5,6]
L=SLL()
L.arrToLL(arr)
L.display()



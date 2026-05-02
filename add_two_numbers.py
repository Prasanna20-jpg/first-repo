# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode=ListNode(-1)
        curr=dummyNode
        carry=0
        temp1=l1
        temp2=l2
        while temp1 != None or temp2 != None:
            sum=carry
            if temp1 != None:
                sum=sum+temp1.val
            if temp2 != None:
                sum=sum+temp2.val
            carry=sum//10
            newNode = ListNode(sum%10)
            curr.next=newNode
            curr=newNode
            if temp1 != None:
                temp1=temp1.next
            if temp2 != None:
                temp2=temp2.next
        if carry != 0:
            newNode=ListNode(carry)
            curr.next=newNode
        return dummyNode.next


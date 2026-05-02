# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        visited=set()
        while temp != None:
            visited.add(temp)
            temp=temp.next
            if temp in visited:
                return True
            

        
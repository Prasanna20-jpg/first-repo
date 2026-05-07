# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        H=set(nums)
        connected = False
        temp = head
        count = 0
        while temp:
            if temp.val in H and not connected:
                connected = True
                count+=1
            elif temp.val not in H and connected:
                connected = False
            temp=temp.next
        return count

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.length(head)
        if l <= 1:
            return 
        middle = (l//2)+1
        current = head
        prev = None
        idx = 1
        while idx < middle:
            prev = current
            current = current.next
            idx += 1
        prev.next = current.next
        current = current.next
        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while(curr):
            counter += 1
            curr = curr.next
        n_node = counter - n + 1

        if n_node == 1:
            return head.next

        curr = head
        counter = 0
        prev = None
        while(curr):
            counter += 1
            if counter == n_node:
                prev.next = curr.next
                break
            
            prev = curr
            curr = curr.next
        return head
            


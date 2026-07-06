# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next:
            return head
        even_head = head.next
        odd_head = head
        even_itr = even_head
        odd_itr = odd_head
        odd_last = odd_head
        while(odd_itr and even_itr and odd_itr.next and even_itr.next):
            even_next = even_itr.next.next
            odd_next = odd_itr.next.next
            odd_itr.next = odd_next
            even_itr.next = even_next
            if odd_next:
                odd_last = odd_next
            even_itr = even_next
            odd_itr = odd_next
        odd_last.next = even_head

        return head
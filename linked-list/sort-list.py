# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        while(curr):
            arr.append(curr.val)
            curr = curr.next
        A = sorted(arr)
        
        itr = head
        ind = 0
        while(itr):
            itr.val = A[ind]
            itr = itr.next
            ind += 1
        return head
            

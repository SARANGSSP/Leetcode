# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = {}
        itr = headA
        while(itr):
            visited[itr] = 1
            itr = itr.next
        itr2 = headB
        while(itr2):
            if (itr2) in visited:
                return itr2
                break
            else:
                itr2 = itr2.next




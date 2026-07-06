# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we store the entire linked list into a frequency array and as soon as a frequency is repeated we store that item  annd check tthe linked list for its position 
        hash = {}
        curr = head
        while(curr):
            if (curr.val,curr.next) not in hash:
                hash[(curr.val,curr.next)] = 1
                curr = curr.next
            else:
                return curr
        return None

            
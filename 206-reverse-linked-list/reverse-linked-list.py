# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val

#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we need to be on head to start anyways
        #we need to store the actual next oif the node since we are going to change it
        #if its head, change it to none
        #go to the next node store it next and change the current nodes next to prev node
        #so we actually need 3 variables then ? 1 to store the current node 1 to store the next and one iterator
        curr = head
        prev = None
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

            
                

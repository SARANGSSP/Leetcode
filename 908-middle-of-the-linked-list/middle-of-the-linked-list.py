# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0

        while(curr):
            count += 1
            curr = curr.next

        iterator = head
        counter = 0
        while(iterator):
            temp = iterator.next
            if counter == (count//2):
                head = iterator
                break
            else:
                iterator = temp
                counter += 1
        return head

                

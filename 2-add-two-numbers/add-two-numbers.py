# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        itr1 = l1
        itr2 = l2
        str1 = ""
        str2 = ""

        while(itr1):
            str1 = str1 + str(itr1.val)
            itr1 = itr1.next
        
        while(itr2):
            str2 = str2 + str(itr2.val)
            itr2 = itr2.next
        
        sumi = str(int(str1[::-1]) + int(str2[::-1]))
        arr = []

        for i in range(len(sumi)):
            arr.append(sumi[i])
        
        arr = arr[::-1]

        tempNode = ListNode(-1)
        curr = tempNode
        for i in range(len(arr)):
            curr.next = ListNode(int(arr[i]))
            curr= curr.next
        
        return tempNode.next


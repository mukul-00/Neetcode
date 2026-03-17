from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def mergeList(l1, l2):

            # for empty lists
            if l1 is None:
                 return l2
            if l2 is None:
                 return l1

            # for choosing starting node
            if(l1.val < l2.val):
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next

            temp = head

            # merging them with sorting
            while(l1 is not None and l2 is not None):
                if(l1.val < l2.val):
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                
                temp = temp.next

            # merge remaining
            if(l1 is not None):
                temp.next = l1
            else:
                temp.next = l2
            
            return head
        return mergeList(list1, list2)

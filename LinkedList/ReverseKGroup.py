from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[Node], k: int) -> Optional[Node]:
        
        # check if at least k nodes exist
        temp = head
        count = 0
        while temp and count < k:
            temp = temp.next
            count += 1
        
        if count < k:
            return head  

        # base case
        if head is None:
            return None
        
        # step 1 : reverse  k nodes
        prev = None
        curr = head
        next = None
        count = 0

        while curr is not None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        
        # step 2 : let recursion handle
        if next is not None:
            head.next = self.reverseKGroup(next, k)
        
        # step 3 : return the reversed LL
        return prev
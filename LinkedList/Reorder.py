# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return

        # 1. Find middle (slow-fast)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        curr = slow.next
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # break list
        slow.next = None

        # 3. Merge both halves
        first, second = head, prev
        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2


# create a list
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("NULL")


# "Main function"
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    head = create_list(arr)

    print("Original List:")
    print_list(head)

    Solution().reorderList(head)

    print("Reordered List:")
    print_list(head)
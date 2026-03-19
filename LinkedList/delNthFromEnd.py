class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    slow, fast = head, head

    # move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # if we need to delete head
    if fast is None:
        return head.next

    # move both pointers
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # delete node
    slow.next = slow.next.next

    return head


# create linked list from array
def create_list(arr):
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


# print linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# main function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = 2

    head = create_list(arr)

    print("Original List:")
    print_list(head)

    head = removeNthFromEnd(head, n)

    print("After Removing Nth Node From End:")
    print_list(head)
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy

        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            # Swap the two nodes
            previous.next = second
            first.next = second.next
            second.next = first

            # Move to the next pair
            previous = first

        return dummy.next
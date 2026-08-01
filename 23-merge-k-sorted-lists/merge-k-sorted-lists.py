import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        dummy = cur = ListNode()

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
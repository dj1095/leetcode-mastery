# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach : Monotonically decreasing stack
        # Time Complexity - O(N) since we are only pushing and popping element only once in inner loop
        # Space Complexity - O(N) for stack
        stack = []
        current = head
        while current:
            while stack and stack[-1].val < current.val:
                # pop lesser value node
                stack.pop()
                if stack:
                    stack[-1].next = current
            stack.append(current)
            current = current.next
        return stack[0]

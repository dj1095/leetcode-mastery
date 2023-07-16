# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        def findSum(l1,l2,carry):
            if not l1 and not l2 and carry <=0:
                return l2
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            result = l1_val + l2_val + carry
            carry = result // 10
            result = result % 10

            head = ListNode(result, None)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            head.next = findSum(l1, l2, carry)
            return head
        return findSum(l1,l2,0)
        
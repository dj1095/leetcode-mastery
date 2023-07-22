# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        debug = head
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        #Finding middle node
        prevMiddle = head
        while fast and fast.next:
            prevMiddle = slow
            slow = slow.next
            fast = fast.next.next
        prevMiddle.next = None

        #Reversing List from Middle Node
        prev= None
        current = slow
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        reverseHead = prev
       # print(reverseHead)

        #Re-ordering the Linked List or Merging
        while reverseHead:
            nextHead , nextReverseHead = head.next, reverseHead.next
            head.next = reverseHead
            reverseHead.next = nextHead
            head, reverseHead = nextHead if nextHead else reverseHead , nextReverseHead
    
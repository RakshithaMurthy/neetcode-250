# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            # Save the next nodes
            temp1 = first.next
            temp2 = second.next
            
            # Rearranging the pointers
            first.next = second
            second.next = temp1
            
            # Move the pointers forward
            first = temp1
            second = temp2
        
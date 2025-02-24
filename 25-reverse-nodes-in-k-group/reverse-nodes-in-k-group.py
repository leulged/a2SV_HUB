# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

    
        def reverser (node):
            prev = None
            p = node
            while p:

                q = p.next
                p.next = prev
                prev = p
                p = q
            return prev
        
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy

 
        while head:
            
            # Check if there is a full group to reverse
            count = 0
            current = head
            while count < k and current:
                current = current.next
                count += 1
          
            # If we have k nodes, proceed to reverse
            if count == k:
                k_group = head
                for _ in range(k-1):
                    k_group = k_group.next
                next_group = k_group.next

                k_group.next = None
                new_group_head = reverser(head)

                # Connect the reversed group back to the list

                prev_group.next = new_group_head
                head.next = next_group
              
                # Move prev_group and head for the next round of reversal
                prev_group = head
                head = next_group

            else:
                     # Not enough nodes to fill a k group, so we are done
                    break

        return dummy.next





    
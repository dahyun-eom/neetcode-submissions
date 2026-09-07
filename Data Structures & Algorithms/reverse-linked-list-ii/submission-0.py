# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy
        for i in range(left-1):
            before_left = before_left.next

        left_node = before_left.next
        right_node = left_node
        for i in range (right-left):
            right_node = right_node.next

        after_right = right_node.next
        right_node.next = None

        #link the middle ones onebyone
        prev = None
        curr = left_node
        new_right = curr

        for i in range(right - left+1):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        #last link for return
        before_left.next = prev
        left_node.next = after_right

        return dummy.next





        



        
    
        return head

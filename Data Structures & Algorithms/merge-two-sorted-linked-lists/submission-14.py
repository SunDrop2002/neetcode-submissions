# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
    
             
        temp_1 = list1
        temp_2 = list2
        curr = ListNode()
        head = curr
    
        while(temp_1 and temp_2):
            if temp_1.val < temp_2.val:
                curr.next = ListNode(temp_1.val)
                temp_1 = temp_1.next
            else :
                curr.next = ListNode(temp_2.val)
                temp_2 = temp_2.next 
            
            curr = curr.next

        while (temp_1):
            curr.next = ListNode(temp_1.val)
            curr = curr.next
            temp_1 = temp_1.next    


        while (temp_2):
            curr.next = ListNode(temp_2.val)
            curr = curr.next
            temp_2 = temp_2.next


        return head.next





        
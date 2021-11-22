# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #incase of a empty linked list create dummy
        dummy = ListNode() 
        tail = dummy
        
        #when both two linked lists are not empty
        while l1 and l2:
            #if l1's value if smaller
            if l1.val < l2.val:
                #let this value join the list
                tail.next = l1
                #goes to next node in l1
                l1 = l1.next
                
            else:
                tail.next = l2
                l2 = l2.next
                
            #updating the tail
            tail = tail.next
            
        #if only l1 is not empty, insert l1 to the list         
        if l1:
            tail.next = l1 
        
        elif l2:
            tail.next = l2
            
        return dummy.next
    

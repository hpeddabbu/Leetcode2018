# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        head= itr= ListNode(0)
        if l1 == None:
            itr.next = l2
            break
        if l2 == None:
            itr.next = l1
            break
        
        while l1 or l2:
            if l1.val < l2.val:
                itr.next = l1
                itr = itr.next
                l1  = l1.next
            else:
                itr.next = l2
                itr = itr.next
                l2 = l2.next
        return itr.next
       """
        head = itr = ListNode(0)

        while l1 and l2:
            
            if l1.val < l2.val:
                itr.next=l1
                
                itr=itr.next
                l1=l1.next
            else:
                itr.next = l2
                
                itr=itr.next
                l2=l2.next
            
        if l1 ==None:
            itr.next=l2
            return head.next
        if l2 ==None:
            itr.next=l1
            return head.next         
        return head
            
                    
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        if carry or l1 or l2:
        """
        carry =0
        
        head= itr= ListNode(0)
        while l1 or l2 or carry:
            v1=0
            v2=0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            itr.val = val
            if carry or l1 or l2:
                itr.next =ListNode(0)
                itr = itr.next
        return head
            
            
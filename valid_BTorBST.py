
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
# we will use range approch to solve this problem
        min_range = float("-inf")
        max_range = float("inf")
        return self.isBST(min_range,max_range,root)
    
    def isBST(self, min_range, max_range, current):
        # if we have successfully reached leaf then it is safe to say that the traversed tree uptil now is BST
        if current == None:
            return True
        # if we are going outof bound then something is not right in BST then return False and also note that condition is <= and >= which eliminates duplicates 
        if current.val <= min_range or current.val >= max_range:
            return False
        
        # now call function recursively with for left subtree it is min_range and max_range == currentNode value 
        # for right subtree it is min_range == currentNode value and max_range 
        return self.isBST(min_range, current.val, current.left) and self.isBST(current.val, max_range, current.right) 
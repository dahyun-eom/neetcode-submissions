# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        

        def helper (n):
            if n is None:
                return
            else:
                helper(n.left)
                res.append(n.val)
                helper(n.right)

        helper(root)
        return res
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     helper(root)
    #     res = []
    #     def helper func (self, n: TreeNode):
    #         if n.left == null:
    #             res.append(n.value)
    #             if n.right != null:
    #                 inorderTraversal(n.right)
    #         else:
    #             helper(n.left)
    #             res.append(n.value)
    #             helper(n.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(node, arr, total):
            if not node:
                return 

            arr.append(node.val)
            total += node.val
            if total == targetSum and not(node.left or node.right):
                ans.append(arr.copy())

            dfs(node.left, arr, total)
            dfs(node.right, arr, total)
            arr.pop()
            
            

        dfs(root, [], 0)
        return ans
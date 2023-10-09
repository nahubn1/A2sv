# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        ans = 0
        def dfs(node, currSum):
            nonlocal ans

            if not node:
                return

            currSum += node.val
            ans += count[currSum-targetSum]
            count[currSum] += 1
            
            dfs(node.left, currSum)
            dfs(node.right, currSum)
            count[currSum] -= 1      

        dfs(root, 0)
        return ans
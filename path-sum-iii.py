# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.hashmap = defaultdict(int)
        self.hashmap[0] = 1

        def countPath(node, rSum):
            if not node:
                return
            
            rSum += node.val
            self.count += self.hashmap[rSum - targetSum]
            self.hashmap[rSum] += 1

            countPath(node.right, rSum)
            countPath(node.left, rSum)

            self.hashmap[rSum] -= 1


        countPath(root, 0)

        return self.count
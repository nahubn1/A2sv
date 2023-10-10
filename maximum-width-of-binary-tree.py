# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        que = deque([(root, 1)])
        ans = 0
        while que:

            ans = max(ans, 1 + max(que, key=lambda x:x[1])[1] - min(que, key=lambda x:x[1])[1])

            for _ in range(len(que)):
                node, i = que.popleft()

                if node.left:
                    que.append((node.left, 2*i))
                if node.right:
                    que.append((node.right, 2*i + 1))
            
        return ans
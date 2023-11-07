# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)

        ans = []
        def dfs(parent, d, node):
            if not node:
                return 

            if node.val in to_delete:
                dfs(-1, "", node.left)
                dfs(-1, "", node.right)
            else:
                new_node = TreeNode(node.val)
                if parent != -1:
                    setattr(parent, d, new_node)
                else:
                    ans.append(new_node)
            
                dfs(new_node, "left", node.left)
                dfs(new_node, "right", node.right)
        
        dfs(-1, "", root)
        return ans






            
            
        
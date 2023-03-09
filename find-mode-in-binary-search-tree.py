# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, node):
        if not node:
            return

        self.count[node.val] += 1
        self.search(node.left)
        self.search(node.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.count = defaultdict(int)
        self.search(root)
        Max = max(self.count, key=self.count.get)

        ans = []
        for num in self.count:
            if self.count[num] == self.count[Max]: 
                ans.append(num)

        return ans
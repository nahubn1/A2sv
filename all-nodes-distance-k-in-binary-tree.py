# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph =  defaultdict(list)

        def create_graph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                create_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                create_graph(node.right)
        
        create_graph(root)

        que = deque([target.val])
        visited = set([target.val])

        level = 0
        while level < k:
            lev_len = len(que)
            for _ in range(lev_len):
                node = que.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        que.append(neighbor)
                        visited.add(neighbor)
 
            level += 1
        
        return list(que)
# 1. easy - Invert Binary Tree
# Time: O(n) Space: O(d)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
# Time: O(n) Space: O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            queue += [node.left, node.right]

        return root

# 2. easy - Maximum Depth of Binary Tree
# Time: O(n) Space: O(h)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# 3. easy - Same Trees
# Time: O(n) Space: O(n)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)
        
# Time: O(n) Space: O(log n)
class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        
        while len(stack) != 0:
            node1, node2 = stack.pop()
            if node1 is not None and node2 is not None and node1.val == node2.val:
                stack += ([(node1.left, node2.left), (node1.right, node2.right)])
            
            elif node1 or node2:
            # if both are False -> skip
            # but  if only one is None, hence
            # True and it'll lead to False
                return False
        
        return True
            

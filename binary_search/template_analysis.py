# 1. Closest Binary Search Tree Value
class Solution:
    # recursive
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result_value = root.val
        
        def dfs(node, result_value):
            if node is None:
                return result_value
            
            if abs(node.val - target) < abs(result_value - target):
                result_value = node.val
            
            if node.val < target:
                return dfs(node.right, result_value)
            elif node.val > target:
                return dfs(node.left, result_value)
            else: # if node.val == target
                return result_value
            
        return dfs(root, result_value)
    
    # iterative
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result_value = root.val
        
        while root:
            if abs(root.val - target) < abs(result_value - target):
                result_value = root.val
            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            elif root.val == target:
                return root.val
        
        return result_value
    
    # binary search
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result = root.val
        while root:
            result = min(result, root.val,
                    key=lambda value: abs(value - target))
            root = root.right if root.val <= target else root.left
        
        return result


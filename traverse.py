# 1. Binary Tree Level Order Traversal

class Solution:
    # first
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while len(queue) != 0:
            
            levels = []
            
            # for-loop remember initial
            # length of array
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    levels.append(node.val)

                    queue.append(node.left)
                    queue.append(node.right)
            
            if levels:
                result.append(levels)
        
        return result
    
    # second
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while len(queue) != 0:
            temp = []
            for q in queue:
                temp.append(q.val)
            
            if temp:
                result.append(temp)
            
            nx = list(queue)
            queue = []
            
            for n in nx:
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
    
        return result

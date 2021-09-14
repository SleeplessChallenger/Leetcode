# 1. binary tree inorder traversal
class Solution:
    # recrusive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        arr = []
        def dfs(node, arr):
            if node.left:
                dfs(node.left, arr)
            arr.append(node.val)
            if node.right:
                dfs(node.right, arr)
        dfs(root, arr)
        return arr
    
   # iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack = []
        node = root
        result = []
        
        while node or len(stack) != 0:
            # will be at start and every time
            # popped node (after while) is not None
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            result.append(node.val)
            node = node.right
        
        return result
    
    # Morris traversal
    '''
    1. if no .left:
        - add current node
        - go .right
    2. else:
        - make current the .right
            of rightmost node
        - go .left 
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        result = []
        curr = root
        
        while curr:
            if curr.left:
                left_node = curr.left
                while left_node.right and left_node.right != curr:
                    left_node = left_node.right
                
                if not left_node.right:
                    left_node.right = curr
                    curr = curr.left
                    
                elif left_node.right == curr:
                    '''
                     -2
                        \
                         2
                        /
                      -1
                      
                      -1 has link to 2. We come back to 2
                      after visiting -1, but now we need
                      to NOT continue infinite loop to -1
                      as we've visitied. Hence, we have
                      check `elif left_node.right == curr:`.
                      We cut connection and go .right of current
                     '''
                    left_node.right = None
                    result.append(curr.val)
                    curr = curr.right
            else:
                result.append(curr.val)
                curr = curr.right
        
        return result

# 2. binary tree preorder traversal
class Solution:
    # dfs
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        arr = []
        def dfs(node, arr):
            arr.append(node.val)
            if node.left:
                dfs(node.left, arr)
            if node.right:
                dfs(node.right, arr)
        
        dfs(root, arr)
        return arr
        
    # bfs
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        result = []
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
            
        
        return result
    
    # Morris traversal
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        node = root
        result = []
        
        while node:
            if node.left:
                curr = node.left
                while curr.right and curr.right != node:
                    curr = curr.right
                    
                if not curr.right:
                    result.append(node.val)
                    curr.right = node
                    node = node.left
                    
                elif curr.right == node:
                # else:
                    curr.right = None
                    node = node.right
            else:
                result.append(node.val)
                node = node.right
        
        return result

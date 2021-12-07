# 1. Maximum Depth of Binary Tree
# new solutions
class Solution:
    # iterative
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]
        answer = 0
        
        while len(stack) != 0:
            node, level = stack.pop()
            if not node.left and not node.right:
                answer = max(answer, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        
        return answer
    
    # recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        not use `return` immediately as it will
        cause code to spit first result of the case
        when node is a leaf
        '''
        if root is None:
            return 0
        
        return self.find_max_depth(root, 1, 1)
    
    def find_max_depth(self, node, ans, level):
        if not node.left and not node.right:
            ans = max(ans, level)
            return ans
        if node.left:
            ans = self.find_max_depth(node.left, ans, level + 1)
        if node.right:
            ans = self.find_max_depth(node.right, ans, level + 1)
        
        return ans

# old solutions
class Solution:
    # recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)) 
    
    # iterative
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [{'node': root, 'depth': 1}]
        total = 0
        while len(stack) != 0:
            info = stack.pop()
            node, curr = info['node'], info['depth']
            if node is None:
                continue
            
            total = max(total, curr)
            stack.append({'node': node.left, 'depth': curr + 1})
            stack.append({'node': node.right, 'depth': curr + 1})
        
        return total

# 2. Count Univalue Subtrees
class Solution:
    # Time: O(n^2)
    '''
    We can have subtree as a Unival tree and
    then we can have the whole tree as a unival
    tree.
    
    => main function is to catch bigger trees
    and isUnival is to deal with subtrees
    '''
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        total = self.countUnivalSubtrees(root.left) + \
            self.countUnivalSubtrees(root.right)
        
        # if the tree itself is a Unival tree -> add 1
        if self.isUnival(root):
            total += 1
        
        return total
    
    def isUnival(self, node):
        if node is None:
            return True
        
        if node.left is not None and node.left.val != node.val:
            return False
        
        if node.right is not None and node.right.val != node.val:
            return False
        
        if self.isUnival(node.left) and self.isUnival(node.right):
            return True
        
        return False
    
    # Time: O(n)
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        total, _ = self.helper(root)
        return total
    
    def helper(self, node):
        if not node:
            return (0, True)
        
        left_count, isUniLeft = self.helper(node.left)
        right_count, isUniRight = self.helper(node.right)
        flag = True
        
        if not isUniLeft or not isUniRight:
            flag = False
        
        if node.left and node.left.val != node.val:
            flag = False
        
        if node.right and node.right.val != node.val:
            flag = False
        
        if flag:
            return (left_count + right_count + 1, True)
        
        return (left_count + right_count, False)

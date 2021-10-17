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

# 4. easy - Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive
    # assuming `root` isn't None in all test cases
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val >= p.val and root.val <= q.val or\
            root.val <= p.val and root.val >= q.val:
            # after `or` will help when: root = 2 p = 2 q = 1
            # => not always p < q!
            return root
        # if tree is smaller than both of nodes ->
        # continue in .right
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # if tree is greater than both of nodes ->
        #  continue  in .left
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
    
    # iterative
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return  root

# 5. easy - Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # 1. if subtree is None => True as None 
        # can be a subtree of any tree
        # 2. if subtree is not None AND main tree
        # is None -> False
        # 3. if both are present -> True: check if 2 trees
        # are identical
        # 4. else: traverse .left and .right sides of the main tree
        # to check if some subtrees are equal to our subtree
        
        if subRoot is None:
            return True
        if root is None:
            return False
        
        if self.identicalTrees(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or\
            self.isSubtree(root.right, subRoot)
    
    def identicalTrees(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False
        return self.identicalTrees(root.left, subRoot.left) and\
            self.identicalTrees(root.right, subRoot.right)


# 6. medium - Validate BST
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validateTree(root, float('-inf'), float('inf'))
    
    def validateTree(self, node, lower, upper):
        if node is None:
            return True
        
        if node.val <= lower or node.val >= upper:
            return False
        
        leftNode = self.validateTree(node.left, lower, node.val)
        return leftNode and self.validateTree(node.right, node.val, upper)

# 7. medium - Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # `not` instead of `is None` as former catches []
        # whilst latter doesn't
        if not preorder or not inorder:
            return None
        
        root = preorder[0]
        idx = 0
        while inorder[idx] != root:
            idx += 1
        
        leftNode = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        rightNode = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return TreeNode(root, leftNode, rightNode)

# 8. medium - Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # brute force
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        def dfs(node, arr):
            if node.left:
                dfs(node.left, arr)
            arr.append(node.val)
            if node.right:
                dfs(node.right, arr)
        dfs(root, arr)
        # edge case: if `arr = [5] k = 0`,
        # then arr[0 - 1] still returns desired result
        # return arr[k - 1]
    
        return arr[abs(1 - k)]
        
    # optimal
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        class_inst = Help(0, None)
        self.getKsmallest(root, k, class_inst)
        return class_inst.prev
    
    def getKsmallest(self, node, k, class_inst):       
        if node is None or k == class_inst.idx:
            return

        self.getKsmallest(node.left, k, class_inst)
        
        if class_inst.idx < k:
            class_inst.idx += 1
            class_inst.prev = node.val
            self.getKsmallest(node.right, k, class_inst)
            

class Help:
    def __init__(self, idx, prev):
        self.idx = idx
        self.prev = prev
        
    # iterative
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

# 9. medium - Serialize and Deserialize BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    object of tree isn't integer intself,
    but class object. Hence if we simply str(node)
    and then try to decode it => error.
    Also make pre-order traversal as we're
    to rebuild the tree further.
    
    + I did preorder traversal. Inorder is also
    possible, especially if combined with binary tree
    construction method. But here it returns. slightly
    different variant of Tree: [2, 1] -> [1, None, 2]
    '''

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ''
        
        arr = []
        self.dfs(root, arr)
        return '&'.join(arr)
    
    def dfs(self, node, arr):
        arr.append(str(node.val))
        if node.left:
            self.dfs(node.left, arr)
        if node.right:
            self.dfs(node.right, arr)

    def deserialize(self, ser: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not ser:
            return None
        
        splitted = ser.split('&')
        result = list(map(lambda x: int(x), splitted))
        return self.rebuildTree(result, float('-inf'), float('inf'))
    
    def rebuildTree(self, nodes, left, right):
        if nodes:
        # to not give None
            if nodes[0] > left and nodes[0] < right:
                node_val = nodes.pop(0)
                node = TreeNode(node_val)
                node.left = self.rebuildTree(nodes, left, node_val)
                node.right = self.rebuildTree(nodes, node_val, right)
                
                return node

# 10. medium - Lowest Common Ancestor of a Binary Tree
class Parent:
    def __init__(self, par, idx):
        self.par = par
        self.idx = idx

    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traverse_tree(root, p, q).par
    
    def traverse_tree(self, node, p, q):
        idx = 0
        leftNode = node.left if node.left else None
        rightNode = node.right if node.right else None
        children = [leftNode, rightNode]
        
        for child in children:
            if child is None:
                continue
            else:
                result = self.traverse_tree(child, p, q)
                if result.par:
                    return result
                idx += result.idx
        
        if node == p or node == q:
            idx += 1
        
        isParent = node if idx == 2 else None
        
        return Parent(isParent, idx)

# Hard chunk

# 11. Binary Tree Maximum Path Sum
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        _, result = self.get_result(root)
        return result
    
    def get_result(self, node):
        if node is None:
            return (0, float('-inf'))
        
        lsb, ls = self.get_result(node.left)
        rsb, rs = self.get_result(node.right)
        mcsb = max(lsb, rsb)
        
        msb = max(mcsb + node.val, node.val)
        mst = max(msb, lsb + node.val + rsb)
        rmps = max(mst, ls, rs)
        
        return (msb, rmps)

# 1. Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ht = {val:idx for idx, val in enumerate(inorder)}
        
        return self.constructTree(0, len(inorder) - 1, ht, inorder, postorder)
    
    def constructTree(self, left, right, ht, inorder, postorder):
        if left > right:
            return None
        
        val = postorder.pop()
        idx = ht[val]
        
        node = TreeNode(val)
        node.right = self.constructTree(idx + 1, right, ht, inorder, postorder)
        node.left = self.constructTree(left, idx - 1, ht, inorder, postorder)
        
        return node

# 2. Populating Next Right Pointers in Each Node II
# O(n) time O(n) space
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        
        queue = [root]
        node = root
        
        while len(queue) != 0:
            size = len(queue)
            
            for i in range(size):
                curr = queue.pop(0)
                if i < size - 1:
                    curr.next = queue[0]
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return node

# 3. Serialize and Deserialize Binary Tree
class Codec:
    '''
    1. we don't `return` as strings will overwrite
        => we use if/else with +=.
    2. we need to keep order with None, hence add as well
    '''
    def serialize(self, root):
        def serializeTree(node, string):
            if not node:
                string += "None,"
            else:
                string += str(node.val) + ','
                string = serializeTree(node.left, string)
                string = serializeTree(node.right, string)
            
            return string
    
        return serializeTree(root, "")

    def deserialize(self, data):
        if not data:
            return None
        
        def deserializeTree(all_nodes):
            # "None" without ',' as we have
            # splitted on ","
            if all_nodes[0] == 'None':
                all_nodes.pop(0)
                return None
            
            node = all_nodes.pop(0)
            treeNode = TreeNode(int(node))
            
            treeNode.left = deserializeTree(all_nodes)
            treeNode.right = deserializeTree(all_nodes)
            
            return treeNode
        
        all_nodes = data.split(',')
        
        return deserializeTree(all_nodes)

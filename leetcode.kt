// 1. Construct Binary Tree from Preorder and Inorder Traversal
class Solution {
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        if((preorder.size == 0) || (inorder.size == 0)) {
            return null
        }
        
        var idx = 0
        val root = preorder[0]
        
        while (idx < inorder.size) {
            if(inorder[idx] == root) {
                break
            }
            idx++
        }
        
        // include first left; exclude root
        val left = this.buildTree(preorder.sliceArray(1..idx), inorder.sliceArray(0..idx - 1))
        val right = this.buildTree(preorder.sliceArray(idx+1..preorder.size - 1), inorder.sliceArray(idx+1..inorder.size - 1))
        
        return TreeNode(root, left, right)
    }
}

// 2. Populating Next Right Pointers in Each Node
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var left: Node? = null
 *     var right: Node? = null
 *     var next: Node? = null
 * }
 */

class Solution {
    fun connect(root: Node?): Node? {
        if(root == null) {
            return null
        }
        this.traverse(root, null, false)
        return root
    }
    
    fun traverse(node: Node?, p: Node?, L: Boolean) {
        if(node == null) return
        
        this.traverse(node.left, node, true)
        
        if(p == null) {
            node.next = null
        } else if(L) {
            node.next = p.right
        } else {
            if(p.next == null) {
                node.next = null
            } else {
                node.next = p.next!!.left
            }
        }
        
        this.traverse(node.right, node, false)
    }
}

// 3 Lowest Common Ancestor of a Binary Tree
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int = 0) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Ancestor(var count: Int, var ancestor: TreeNode?)



class Solution {
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        return this.traverse(root, p, q).ancestor
    }
    
    fun traverse(node: TreeNode?, p: TreeNode?, q: TreeNode?): Ancestor {
        var idx = 0
        
        val nodeLeft: TreeNode? = node?.left ?: null
        val nodeRight: TreeNode? = node?.right ?: null
        
        val arr = listOf(nodeLeft, nodeRight)
        
        for(child in arr) {
            if(child == null) {
                continue
            } else {
            
            val result = this.traverse(child, p, q)
            
            if(result.ancestor != null) return result
            
            idx += result.count
            }
        }
        
        if((p == node) || (q == node)) {
            idx++
        }
        
        val isParent: TreeNode? = if(idx == 2) node else null
        
        val finalResult = Ancestor(idx, isParent)
        
        return finalResult
    }
}

// 4. Count Univalue Subtrees
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun countUnivalSubtrees(root: TreeNode?): Int {
        val (result, _) = this.traverseTree(root)
        return result
    }
    
    fun traverseTree(node: TreeNode?): Pair<Int, Boolean> {
        if(node == null) return Pair(0, true)
        
        val (leftCount, leftUni) = this.traverseTree(node.left)
        val (rightCount, rightUni) = this.traverseTree(node.right)
        var flag: Boolean = true
        
        if(leftUni != true || rightUni != true) flag = false
        
        if(node.left != null && node.left.`val` != node.`val`) flag = false
        
        if(node.right != null && node.right.`val` != node.`val`) flag = false
        
        if(flag == true) {
            return Pair((leftCount + rightCount + 1), true)
        } else return Pair((leftCount + rightCount), false)
        
    }
}

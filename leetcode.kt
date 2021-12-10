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

// 5. Populating Next Right Pointers in Each Node II
class Solution {
    fun connect(root: Node?): Node? {
        if(root == null) return null
        
        var queue = mutableListOf<Node?>(root)
        val node_result = root
        
        while(queue.size != 0) {
            val curr_size = queue.size
            
            for(i in 0 until curr_size){
                val node: Node? = queue.removeAt(0)
                
                if(i < curr_size - 1){
                    node!!.next = queue[0]
                }
                
                if(node!!.left != null) {
                    queue.add(node!!.left)
                }
                
                if(node!!.right != null) {
                    queue.add(node!!.right)
                }
            }
        }
        
        return node_result
    }
}

// 6. Serialize and Deserialize Binary Tree
class Codec() {
    fun serialize(root: TreeNode?): String {
        if(root == null) return ""
        
        var all_nodes = mutableListOf<Int?>()
        
        fun serializeTree(node: TreeNode?) {
            if(node == null) {
                all_nodes.add(null)
            } else {
                all_nodes.add(node.`val`)
                
                serializeTree(node.left)
                serializeTree(node.right)
            }
        }
        
        
        serializeTree(root)
        
        return all_nodes.joinToString()
    }

    // Decodes your encoded data to tree.
    fun deserialize(data: String): TreeNode? {
        if(data == "") return null
        
        fun deserializeTree(nodes: MutableList<String>): TreeNode? {
            // crucial to specify MutableList in params
            if(nodes[0] == "null") {
                nodes.removeAt(0)
                return null
            }
            
            var strNode: String = nodes[0]
            // var strNode: String = nodes.removeAt(0)
            
            nodes.removeAt(0)
            val node: TreeNode = TreeNode(strNode.toInt())
            node.left = deserializeTree(nodes)
            node.right = deserializeTree(nodes)
            
            return node
        }
        
        var temp = data.split(',').map { i -> i.trim() }.toMutableList()
        // var temp = data.split(',').toMutableList()
        
        return deserializeTree(temp)
    }
}

// 7. Binary Search
class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var left: Int = 0
        var right: Int = nums.size - 1
        
        while(left <= right) {
            var middle: Int = (left + right) // 2
            
            if(nums[middle] == target) return middle
            
            else if(nums[middle] > target) {
                right = middle - 1
            } else {
                left = middle + 1
            }
        }
        
        return -1
    }
}

// 8. Sqrt(x)
class Solution {
    // binary search solution
    fun mySqrt(x: Int): Int {
        if(x < 2) return x
        
        var left = 2
        var right = x / 2
        
        while(left <= right) {
            var midd = left + (right - left) / 2
            var squaredMidd: Long = midd.toLong() * midd.toLong()
            
            
            if(squaredMidd > x) right = midd - 1
            else if (squaredMidd < x) left = midd + 1
            else return midd
        }
        
        return right
    }
}

// 9. Guess Number Higher or Lower
class Solution:GuessGame() {
    override fun guessNumber(n:Int):Int {
        var left = 1
        var right = n
        
        while (true){
            var midd = left + (right - left) / 2
            var result = guess(midd)
            
            if(result == 0){
                return midd
            } else if(result == -1) {
                right = midd - 1
            } else if(result == 1) {
                left = midd + 1
            }
        }
    }
}

// 10. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            midd = (left + right) // 2
            
            if nums[midd] == target:
                return midd
            
            # in cases when left == right
            # we need to proceed, i.e. change value
            # of left || right, hence <= is essential
            # AND particularly in this `elif`.
            # I.e. take [3,1] t=0
            elif nums[midd] > nums[left]:
                if nums[left] <= target and target < nums[midd]:
                    right = midd - 1
                else:
                    left = midd + 1
                    
            elif nums[midd] <= nums[right]:
                if nums[right] >= target and target > nums[midd]:
                    left = midd + 1
                else:
                    right = midd - 1

        return -1

// 11. First Bad Version
/* The isBadVersion API is defined in the parent class VersionControl.
      def isBadVersion(version: Int): Boolean = {} */

class Solution: VersionControl() {
    // first version
    override fun firstBadVersion(n: Int) : Int {
    
        var left: Int = 1
        var right: Int = n
        
        while (left <= right) {
            var midd = left + (right - left) / 2
            val result: Boolean = isBadVersion(midd)
            
            if(result == false) {
                left = midd + 1
            } else if(isBadVersion(midd - 1) == false) {
                return midd
            } else {
                right = midd - 1
            }
            
        }
        
        return -1
    }
    
    // second version
    override fun firstBadVersion(n: Int) : Int {
        var left = 1
        var right = n
        
        while (left < right) {
            var midd = left + (right - left) / 2
            if(isBadVersion(midd)) {
                right = midd
            } else {
                left = midd + 1
            }
        }
        
        return left
}
}


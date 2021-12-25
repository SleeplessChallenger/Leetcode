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

// 12. Find Peak Element
class Solution {
    // O(n) time
    fun findPeakElement(nums: IntArray): Int {
        for(i in 0 until nums.size - 1) {
            if(nums[i] > nums[i+1]) return i
        }
        
        return nums.size - 1
    }
    
    // O(log n) time
    fun findPeakElement(nums: IntArray): Int {
        var left: Int = 0
        var right: Int = nums.size - 1
        
        while (left < right) {
            var midd: Int = left + (right - left) / 2
            if(nums[midd] < nums[midd + 1]) {
                left = midd + 1
            } else if(nums[midd] > nums[midd + 1]) {
                right = midd
            }
    }
        return left
}
}

// 13. Find Minimum in Rotated Sorted Array
class Solution {
    fun findMin(nums: IntArray): Int {
        if(nums.size == 1) {
            return nums[0]
        }
        
        var left: Int = 0
        var right: Int = nums.size - 1
        
        if(nums[left] < nums[right]) {
            return nums[left]
        }
        
        while (left < right) {
            var midd: Int = left + (right - left) / 2
            
            if(nums[midd] > nums[midd + 1]) {
                return nums[midd + 1]
            } else if(nums[midd] < nums[midd - 1]) {
                return nums[midd]
            } else if(nums[midd] > nums[left]) {
                left = midd + 1
            } else if(nums[midd] < nums[right]) {
                right = midd - 1
            }
        }
        
        return -1
    }
}

// 14. Search for a Range
class Solution {
    fun searchRange(nums: IntArray, target: Int): IntArray {
        var result: IntArray = intArrayOf(-1,-1)
        this.calc_nums(nums, result, true, target)
        this.calc_nums(nums, result, false, target)
        
        return result
    }
    
    fun calc_nums(nums: IntArray, result: IntArray, goLeft: Boolean, t: Int) {
        var left: Int = 0
        var right: Int = nums.size - 1
        
        while (left <= right) {
            var midd: Int = left + (right - left) / 2
            if(nums[midd] > t) {
                right = midd - 1
            } else if(nums[midd] < t) {
                left = midd + 1
            } else {
                if(goLeft == true) {
                    if(midd == 0 || nums[midd - 1] != t) {
                        result[0] = midd
                        return
                    } else {
                        right = midd - 1
                    }
                } else {
                    if(midd == nums.size - 1 || nums[midd + 1] != t) {
                        result[1] = midd
                        return
                    } else {
                        left = midd + 1
                    } 
                }
            }
        }
    }
}

// 15. Search in a Sorted Array of Unknown Size
/**
 * // This is ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *     fun get(index: Int): Int {}
 * }
 */

class Solution {
    fun search(reader: ArrayReader, target: Int): Int {
        var left: Int = 0
        var right: Int = 1
        
        while(target > reader.get(right)) {
            left = right
            right = right * 2
        }
        
        while(left <= right) {
            var midd: Int = (left + (right - left) / 2) //.toInt()
            val curr_result = reader.get(midd)
            
            if(curr_result == target) {
                return midd
            } else if(curr_result > target) {
                right = midd - 1
            } else if(curr_result < target) {
                left = midd + 1
            }
        }
        
        return -1
    }
}

// 16. Closest Binary Search Tree Value
import kotlin.math.*


class Solution {
    
    // recursive
    fun closestValue(root: TreeNode?, target: Double): Int {
        var smallest: Int = root!!.`val`
        
        fun dfs(node: TreeNode, smallest: Int, target: Double):Int {
            // if(node == null) {
            //     return smallest
            // }
            
            var newSmallest = smallest
            
            if(abs(node.`val` - target) < abs(smallest - target)) {
                newSmallest = node.`val`
            }
            
            if(node.`val` > target && node.left != null) {
                return dfs(node.left!!, newSmallest, target)
            } else if(node.`val` < target && node.right != null) {
                return dfs(node.right!!, newSmallest, target)
            } else {
                return newSmallest
            }
        }

        return dfs(root, smallest, target)
    }
    
    // iterative
    fun closestValue(root: TreeNode?, target: Double): Int {
        var smallest = root!!.`val`
        var node = root
        
        while(node != null) {
            if(abs(node.`val` - target) < abs(smallest - target)) {
                smallest = node.`val`
            }
            
            if(node.`val` > target && node.left != null) {
                node = node.left!!
            } else if(node.`val` < target && node.right != null) {
                node = node.right!!
            } else {
                break
            }
        }
        
        return smallest
    }
}

// 17. Pow(x, n)
import kotlin.math.*


// Time: O(n)
class Solution {
    fun myPow(x: Double, n: Int): Double {
        if(n >= 0) {
            return this.calcPow(x, n, 1.0)
        } else {
            return this.calcPow(1/x, abs(n), 1.0)
        }
    }
    
    fun calcPow(x: Double, n: Int, base: Double): Double {
        var newBase: Double = base
        
        for(i in 0 until n) {
            newBase = newBase * x
        }
        
        return newBase
    }

    // Time: O(log n)
    fun myPow(x: Double, n: Int): Double {
        if(n >= 0) {
            return this.calcPow(x, n)
        } else {
            return this.calcPow(1/x, abs(n))
        }
    }
    
    fun calcPow(x: Double, n: Int): Double {
        // 1 / 2 = 0
        if(n == 0) {
            return 1.0
        }
        // if n = 1 && x = 5: 1.0 * 1.0 * 5
        // x^2 * x^2 * x = 5
        var res: Double = this.calcPow(x, n/2)
        
        if(n % 2 == 0) {
            return res * res
        } else {
            return res * res * x
        }
    }
}

// 18. Valid Perfect Square
class Solution {
    fun isPerfectSquare(num: Int): Boolean {
        if(num <= 2) {
            return true
        }
        
        var left = 0
        var right = num / 2
        
        while(left <= right) {
            var midd_num = left + (right - left) / 2
            var double_midd = midd_num.toLong() * midd_num.toLong()
            
            if(double_midd < num) {
                left = midd_num + 1
            } else if(double_midd > num) {
                right = midd_num - 1
            } else {
                return true
            }
        }
        
        return false
    }
}

// 19. Find Smallest Letter Greater Than Target
class Solution {
    fun nextGreatestLetter(letters: CharArray, target: Char): Char {
        if(letters.last() <= target || letters.first() > target) {
            return letters.first()
        }
        
        var left: Int = 0
        var right: Int = letters.size - 1
        
        while(left <= right) {
            var midd: Int = left + (right - left) / 2
            
            if(letters[midd] <= target) {
                left = midd + 1
            } else {
                right = midd - 1
            }
        }
        
        return letters[left]
    }
}

// 20. Find K Closest Elements
import kotlin.math.*


class Solution {
    // with sort: O(n * log n)
    fun findClosestElements(arr: IntArray, k: Int, x: Int): List<Int> {
        // 1. sort by diff between num & x
        // 2. traverse with `k` as idx and put in arr
        // 3. sort final array
        val sortedArr = arr.sortedBy {abs(it - x)}
        // sorted(arr, key=lambda num: abs(num-x))

        var result: MutableList<Int> = mutableListOf<Int>()
        
        for(i in 0 until k) {
            result.add(sortedArr[i])
        }
        
        result.sort()
        return result
    }

    // O(log n)
    fun findClosestElements(arr: IntArray, k: Int, x: Int): List<Int> {
        var left: Int = 0
        var right: Int = arr.size - k
        
        while(left < right) {
            var midd: Int = left + (right - left) / 2
            
            if(x - arr[midd] > arr[midd + k] - x) {
                left = midd + 1
            } else {
                right = midd
            }
        }
        
        return arr.slice(left..left+k-1)
    }
}

// 21. Find Minimum in Rotated Sorted Array II
class Solution {
    fun findMin(nums: IntArray): Int {
        var left: Int = 0
        var right: Int = nums.size - 1
        
        while(left <= right) {
            var mid: Int = left + (right - left) / 2
            if(nums[mid] < nums[right]) {
                right = mid
            } else if(nums[mid] > nums[right]) {
                left = mid + 1
            } else  { // nums[mid] == nums[right]
                right = right - 1
            }
        }
        
        return nums[left]
    }
}

// 22. Intersection of Two Arrays
class Solution {
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        if(nums1.size < nums2.size) {
            return this.get_intersection(nums1, nums2)
        } else {
            return this.get_intersection(nums2, nums1)
        }
    }
    
    fun get_intersection(small: IntArray, big: IntArray): IntArray {
        
        var result = mutableListOf<Int>()
        
        val small_set = small.toSet()
        val big_set = big.toSet()
        
        for(num in small_set) {
            if(num in big_set) {
                result.add(num)
            }
        }
        
        return result.toIntArray()
    }
}

// 23. Intersection of Two Arrays II
class Solution {
    fun intersect(nums1: IntArray, nums2: IntArray): IntArray {
        if(nums1.size < nums2.size) {
            return this.get_nums(nums1, nums2)
        } else {
            return this.get_nums(nums2, nums1)
        }
    }
    
    fun get_nums(small: IntArray, big: IntArray): IntArray {
        var result = mutableListOf<Int>()
        var ht = mutableMapOf<Int, Int>()
        
        for(num in big) {
            if(!ht.containsKey(num)){
                ht[num] = 0
            }
            
            ht[num] = ht[num]!! + 1
             
        }

        for(num in small) {
            if(ht.containsKey(num) && ht[num] != 0) {
                result.add(num)
                ht[num] = ht[num]!! - 1
            }
        }
        
        return result.toIntArray()
    }
}

class Solution {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var result = mutableListOf<Int>()
        
        for(i in 0 until numbers.size - 1) {
            var left = i + 1
            var right = numbers.size - 1
            
            var curr_diff = target - numbers[i]
            var flag: Boolean = false
            
            while(left <= right) {
                var midd = left + (right - left) / 2
                if(numbers[midd] == curr_diff) {
                    result.add(i+1)
                    result.add(midd+1)
                    break
                } else if(numbers[midd] < curr_diff) {
                    left = midd + 1
                } else {
                    right = midd - 1
                }
            }
            
            if(result.size != 0) {
                break
            }
        }
        
        return result.toIntArray()
    }
}

// 24. Find the Duplicate Number
import kotlin.math.*


class Solution {
    fun findDuplicate(nums: IntArray): Int {
        var curr_abs: Int = 0
        
       for(num in nums) {
            curr_abs = abs(num)
            if(nums[curr_abs-1] < 0) {
                break
            }
            nums[curr_abs-1] *= -1
       }
       
       return curr_abs
    }
    
    fun findDuplicate(nums: IntArray): Int {
        var slow: Int = nums[0]
        var fast: Int = nums[0]
        
        while(true) {
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if(slow == fast) {
                break
            }
        }
        
        var newStart: Int = nums[0]
        while(newStart != fast) {
            fast = nums[fast]
            newStart = nums[newStart]
        }
        
        return newStart
    }
}

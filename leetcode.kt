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
    
    fun findDuplicate(nums: IntArray): Int {
        var left: Int = 1
        var right: Int = nums.size - 1
        
        var duplicate: Int = 0
        
        while(left <= right) {
            var midd: Int = left + (right - left) / 2
            var count = this.get_values(midd, nums)
            
            if(count > midd) {
                duplicate = midd
                right = midd - 1
            } else {
                left = midd + 1
            }
        }
        
        return duplicate
    }
    
    fun get_values(midd: Int, nums: IntArray): Int {
        var count: Int = 0
        
        for(num in nums) {
            if(num <= midd) {
                count += 1
            }
        }
        
        return count
    }
}

// 25. Inorder Successor in BST
class Solution {
    fun inorderSuccessor(root: TreeNode?, p: TreeNode?): TreeNode? {
        var currNode: TreeNode? = null
        var node = root
        
        while(node != null) {
            if(node.`val` > p!!.`val`) {
                currNode = node
                node = node.left
            } else {
                node = node.right
            }
        }
        
        return currNode
    }

// 26. Search in a Binary Search Tree
class Solution {
    fun searchBST(root: TreeNode?, `val`: Int): TreeNode? {
        if(root == null) {
            return null
        }
        
        if(root.`val` > `val`) {
            return this.searchBST(root.left, `val`)
        } else if(root.`val` < `val`) {
            return this.searchBST(root.right, `val`)
        } else {
            return root
        }
    }
}


// 27. Median of Two Sorted Arrays
import kotlin.math.*


class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        if(nums1.size > nums2.size) {
            return this.get_median(nums2, nums1)
        } else {
            return this.get_median(nums1, nums2)
        }
    }
    
    fun get_median(small: IntArray, big: IntArray): Double {
        var left: Int = 0
        var right: Int = small.lastIndex
        
        var total: Int = small.size + big.size
        var half_size: Int = total / 2

        while(true) {    
            // we need `- 1 // 2` become -1, not 0 as it's now
            var midd: Int = left + (right - left) % 2
            var midd_big: Int = half_size - midd - 2
            var small_midd_val: Int = 0
            var small_midd_right_val: Int = 0
            var big_midd_val: Int = 0
            var big_midd_right_val: Int = 0
            
            if(midd >= 0) {
                small_midd_val = small[midd]
            } else {
                //const val NEGATIVE_INFINITY: Float
                small_midd_val = -1000000
            }
            
            if(midd+1 <= small.lastIndex) {
                small_midd_right_val = small[midd+1]
            } else {
                small_midd_right_val = 1000000
            }
            
            if(midd_big >= 0) {
                big_midd_val = big[midd_big]
            } else {
                big_midd_val = -1000000
            }
            
            if(midd_big+1 <= big.lastIndex) {
                big_midd_right_val = big[midd_big+1]
            } else {
                big_midd_right_val = 1000000
            }
            
            if(small_midd_val <= big_midd_right_val && big_midd_val <= small_midd_right_val) {
                if(total % 2 == 0) {
                    return (max(small_midd_val, big_midd_val).toDouble() + min(small_midd_right_val, big_midd_right_val).toDouble()) / 2
                } else {
                    return min(small_midd_right_val, big_midd_right_val).toDouble()
                }
            } else if(small_midd_val > big_midd_right_val) {
                right = midd - 1
            } else {
                left = midd + 1
            }
            
        }
    }
}

// 28. Kth Largest Element in an Array
import kotlin.math.*

class Solution {
    brute-force
    fun findKthLargest(nums: IntArray, k: Int): Int {
        nums.sort()
        return nums[nums.size - k]
    }
    
    hashtable
    fun findKthLargest(nums: IntArray, k: Int): Int {
        var max_value = -1
        var hashtable = mutableMapOf<Int,Int>()
        var t: Int = k
        
        for(num in nums) {
            max_value = max(max_value, num)
            
            if(!hashtable.containsKey(num)) {
                hashtable[num] = 0
            } 
            
            hashtable[num] = hashtable[num]!! + 1
        }

        while(true) {
            if(t == 1 && hashtable.containsKey(max_value)) {
                return max_value
            } else {
                if(hashtable.containsKey(max_value)) {
                    hashtable[max_value] = hashtable[max_value]!! - 1
                    t -= 1
                    if(hashtable.get(max_value) == 0) {
                        max_value -= 1
                    }
                } else {
                    max_value -= 1
                }
            }
        }
    }
    
    // Quickselect
    fun findKthLargest(nums: IntArray, k: Int): Int {
        var t: Int = nums.size - k
        return this.get_result(nums, t, 0, nums.size - 1)
    }
    
    fun get_result(nums: IntArray, t: Int, start: Int, end: Int): Int {  
        var end = end
        var start = start
        
        while(true) {
            var pivot: Int = start
            var left: Int = pivot + 1
            var right: Int = end
            
            while(left <= right) {
                if(nums[pivot] < nums[left] && nums[pivot] > nums[right]) {
                    this.swap(nums, left, right)
                }
                
                if(nums[pivot] >= nums[left]) {
                    left += 1
                }
                
                if(nums[pivot] <= nums[right]) {
                    right -= 1
                }
                
//                 when {
//                     nums[pivot] < nums[left] && nums[pivot] > nums[right] -> {
//                         this.swap(nums, left, right)
//                     }
//                 }
//                 when {
//                     nums[pivot] >= nums[left] -> {
//                         left += 1
//                     }
//                 }
//                 when {
//                     nums[pivot] <= nums[right] -> {
//                         right -= 1
//                     }
//                 }
            }
            
            this.swap(nums, right, pivot)
            
            if(right > t) {
                end = right - 1
            } else if(right < t) {
                start = right + 1
            } else {
                return nums[t]
            }
        }
    }
    // [3,2,1,5,6,4] 2
    // [2,1] 2
    fun swap(nums: IntArray, l: Int, r: Int) {
        // nums[l], nums[r] = nums[r], nums[l]
        val a = nums[l]
        val b = nums[r]
        nums[l] = b
        nums[r] = a
    }
}

// 29. Insert into a Binary Search Tree
class Solution {
    fun insertIntoBST(root: TreeNode?, `val`: Int): TreeNode? {
        if(root == null) {
            return TreeNode(`val`)
        }
        fun putValue(root: TreeNode?, newNode: Int) {
            if(root!!.`val` < newNode) {
                if(root.right != null) {
                    putValue(root.right, newNode)
                } else {
                    root!!.right = TreeNode(newNode)
                } 
            } else {
                if(root.left != null) {
                    putValue(root.left, newNode)
                } else {
                    root!!.left = TreeNode(newNode)
                }
            }
        }
        putValue(root, `val`)
        return root
    }
}

// 30. Binary Search Tree Iterator
class BSTIterator(root: TreeNode?) {
    private var nodes = mutableListOf<Int>()
    private var idx: Int = 0
    
    init {
        this.traverseNodes(root)
    }
    
    
    fun next(): Int {
        val return_node = this.nodes[this.idx]
        this.idx += 1
        return return_node
    }

    fun hasNext(): Boolean {
        when {
            this.idx < this.nodes.size -> {
                return true
            } else -> {
                return false
            }
        }
    }
    
    fun traverseNodes(node: TreeNode?) {
        if(node!!.left != null) {
            this.traverseNodes(node.left)
        }
        this.nodes.add(node.`val`)
        if(node!!.right != null) {
            this.traverseNodes(node.right)
        }
    }

}

// O(1) Space
class BSTIterator(root: TreeNode?) {

    private var stack = mutableListOf<TreeNode>()
    
    init {
        this.goLeft(root)    
    }
    
    fun next(): Int {
        var currNode: TreeNode = this.stack[this.stack.size - 1]
        this.stack.remove(currNode)
        // var currNode = this.stack.removeLast()
        
        if(currNode.right != null) {
            this.goLeft(currNode.right)
        }
        return currNode.`val`
    }
    
    fun hasNext(): Boolean {
        return this.stack.size != 0
    }
    
    fun goLeft(node: TreeNode?) {
        var currNode: TreeNode? = node
        
        while(currNode != null) {
            this.stack.add(currNode)
            currNode = currNode.left
        }
    }
    
}

// 31. Delete Node in a BST
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
    fun deleteNode(root: TreeNode?, key: Int, p: TreeNode?=null): TreeNode? {
        var node: TreeNode? = root
        var parent: TreeNode? = p
        
        while(node != null) {
            if(node.`val` > key) {
                parent = node
                node = node!!.left
            } else if(node.`val` < key) {
                parent = node
                node = node!!.right
            } else {
                if(node.left != null && node.right != null) {
                    val currNodeValue: Int = this.findNode(node.right)
                    node.`val` = currNodeValue
                    this.deleteNode(node.right, node.`val`, node)
                } else if(parent == null) {
                    if(node.left != null) {
                        node.right = node.left.right
                        node.`val` = node.left.`val`
                        node.left = node.left.left
                    } else if(node.right != null) {
                        node.left = node.right.left
                        node.`val` = node.right.`val`
                        node.right = node.right.right
                    } else {
                        return null
                    }
                } else if(parent.left == node) {
                    parent.left = when {
                        node.right != null -> {
                            node!!.right 
                        } else -> {
                            node!!.left
                        }
                    }
                } else if(parent.right == node) {
                    parent.right = when {
                        node.left != null -> {
                            node!!.left
                        } else -> {
                            node!!.right
                        }
                    }
                } else {
                    break
                }
            }
        }
        
        return root
    }
    
    fun findNode(node: TreeNode?): Int {
        var currNode: TreeNode? = node
        while(currNode!!.left != null) {
            currNode = currNode!!.left
        }
        
        return currNode!!.`val`
    }
}

// 32. Validate Binary Search Tree
class Solution {
    fun isValidBST(root: TreeNode?): Boolean {
        if(root == null) {
            return true
        }
        return this.checkValid(root.left, null, root.`val`) && this.checkValid(root.right, root.`val`, null)
    }
    
    fun checkValid(node: TreeNode?, lower: Int?, upper: Int?): Boolean {
        if(node == null) {
            return true
        }
        val currVal: Int = node.`val`
        if((lower == null || currVal > lower!!) && (upper == null || currVal < upper!!)) {
            return this.checkValid(node.left, lower, currVal) && this.checkValid(node.right, currVal, upper)
        }
        return false
    }
}

// 33. Contains Duplicate
class Solution {
    // sorting
    fun containsDuplicate(nums: IntArray): Boolean {
        nums.sort()
        for(i in 1 until nums.size) {
            if(nums[i] == nums[i-1]) {
                return true
            }
        }
        return false
    }
    
    // ht
    fun containsDuplicate(nums: IntArray): Boolean {
        var ht = mutableMapOf<Int,Boolean>()
        
        for(num in nums) {
            if(ht.containsKey(num)) {
                return true
            }
            ht[num] = true
        }
        
        return false
    }
}

// 34. Balanced Binary Tree
import kotlin.math.*

class TreeInfo(val height: Int, val isBalanced: Boolean)

class Solution {
    // first ver.
    fun isBalanced(root: TreeNode?): Boolean {
        return this.traverseTree(root).isBalanced
    }
    
    fun traverseTree(root: TreeNode?): TreeInfo {
        if(root == null) {
            return TreeInfo(-1, true)
        }
        
        val leftBranch: TreeInfo = this.traverseTree(root.left)
        val rightBranch: TreeInfo = this.traverseTree(root.right)
        
        val isBalanced: Boolean = leftBranch.isBalanced &&
            rightBranch.isBalanced &&
            abs(leftBranch.height - rightBranch.height) <= 1
        
        val currHeight = 1 + max(leftBranch.height, rightBranch.height)
        
        return TreeInfo(currHeight, isBalanced)
    }
    
    // second ver.
    fun isBalanced(root: TreeNode?): Boolean {
        fun traverseLevels(node: TreeNode?): Int {
            if(node == null) {
                return 0
            }
            return max(traverseLevels(node.left), traverseLevels(node.right)) + 1
        }
        
        if(root == null) {
            return true
        }
        
        return abs(traverseLevels(root.left) - traverseLevels(root.right)) <= 1 &&
            this.isBalanced(root.left) && this.isBalanced(root.right)
    }
}

// 35. Range Sum of BST
class Solution {
    // Non-optimal solution
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        var allNodes = mutableListOf<Int>()
        
        fun traverse(node: TreeNode?): Unit {
            if(node == null) {
                return
            }
            if(node.`val` >= low && node.`val` <= high) {
                allNodes.add(node.`val`)
            }
            
            if(node.left != null) {
                traverse(node.left)
            }
            
            if(node.right != null) {
                traverse(node.right)
            }
        }
        
        traverse(root)
        
        var total: Int = 0
        for(node in allNodes) {
            total += node
        }
        
        return total
    }
}
    
    // Optimal solution
    
class Solution(var total:Int = 0) { 
    
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        this.traverseNodes(root, low, high)
        
        return this.total
    }
    
    fun traverseNodes(node: TreeNode?, low: Int, high: Int): Unit {
        if(node == null) {
            return
        }
        
        if(node!!.`val` >= low && node.`val` <= high) {
            this.total += node.`val`
        }
        
        if(node.`val` > low) {
            this.traverseNodes(node.left, low, high)
        }
        
        if(node.`val` < high) {
            this.traverseNodes(node!!.right, low, high)
        }
        
        return
    }
}

// 36. Binary Search Tree Iterator

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
class BSTIterator(root: TreeNode?) {
    private var nodes = mutableListOf<Int>()
    private var idx: Int = 0
    
    init {
        this.traverseNodes(root)
    }
    
    
    fun next(): Int {
        val return_node = this.nodes[this.idx]
        this.idx += 1
        return return_node
    }

    fun hasNext(): Boolean {
        when {
            this.idx < this.nodes.size -> {
                return true
            } else -> {
                return false
            }
        }
    }
    
    fun traverseNodes(node: TreeNode?) {
        if(node!!.left != null) {
            this.traverseNodes(node.left)
        }
        this.nodes.add(node.`val`)
        if(node!!.right != null) {
            this.traverseNodes(node.right)
        }
    }

}

// O(1) Space
class BSTIterator(root: TreeNode?) {

    private var stack = mutableListOf<TreeNode>()
    
    init {
        this.goLeft(root)    
    }
    
    fun next(): Int {
        var currNode: TreeNode = this.stack[this.stack.size - 1]
        this.stack.remove(currNode)
        // var currNode = this.stack.removeLast()
        
        if(currNode.right != null) {
            this.goLeft(currNode.right)
        }
        return currNode.`val`
    }
    
    fun hasNext(): Boolean {
        return this.stack.size != 0
    }
    
    fun goLeft(node: TreeNode?) {
        var currNode: TreeNode? = node
        
        while(currNode != null) {
            this.stack.add(currNode)
            currNode = currNode.left
        }
    }
    
}


// concise Kotlin-Style: val + iterator
class BSTIterator(root: TreeNode?) {
    private val nodes = root?.let{ traverseNodes(it) } ?: emptyList()
    private val nodeIterator = nodes.iterator()
    
    fun next(): Int {
        return nodeIterator.next()
    }
    
    fun hasNext(): Boolean {
        return nodeIterator.hasNext()
    }
    
    fun traverseNodes(node: TreeNode): List<Int> {
        val leftNodes = node.left?.let{ traverseNodes(it) } ?: emptyList()
        
        // val leftNodes = if(node.left != null) {
        //     traverseNodes(node.left)
        // } else {
        //     emptyList()
        // }
        
        val rightNodes = node.right?.let { traverseNodes(it) } ?: emptyList()
        
        return leftNodes + node.`val` + rightNodes
    }    
}

// 37. Sum of Left Leaves
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
    
    // recursive
    var total: Int = 0
    
    fun sumOfLeftLeaves(root: TreeNode?): Int {
        if(root == null) {
            return 0
        }
        
        start_traversal(root)
         
         return total
    }
    
    fun start_traversal(node: TreeNode): Unit {
        if(node.left != null && node.left.left == null
            && node.left.right == null) {
            total += node.left.`val`
        }
        
        if(node.left != null) {
            start_traversal(node.left)
        }
        
        if(node.right != null) {
            start_traversal(node.right)
        }
    }
    
    // iterative
    
    var stack = mutableListOf<TreeNode>()
    var total: Int = 0
    
    fun sumOfLeftLeaves(root: TreeNode?): Int {
        if(root == null) {
            return 0
        }
        
        traverse_tree(root)
        
        return total
    }
        
    
    fun traverse_tree(root: TreeNode): Unit {
        stack.add(root)
        
        while(stack.size != 0) {
            val currNode = stack[stack.size - 1]
            stack.remove(currNode)
            
            if(currNode.left != null &&
                    currNode.left.left == null &&
                    currNode.left.right == null) {
                total += currNode.left.`val`
            }
            
            // append right at first as
            // `stack` priotirize tip
            // => put `.left` afterwards
            if(currNode.right != null) {
                stack.add(currNode.right)
            }
            
            if(currNode.left != null) {
                stack.add(currNode.left)
            }
        }
    }
    
    // morris traversal
    fun sumOfLeftLeaves(root: TreeNode?): Int {
        if(root == null) {
            return 0
        }
        
        var total: Int = 0
        var node: TreeNode = root
        
        while(node != null) {
            if(node.left == null) {
                if(node.right != null) {
                    node = node.right
                } else {
                    break
                }
            } else {
                // if .left != null
                var currLeftNode = node.left
                if(currLeftNode.left == null && currLeftNode.right == null) {
                    total += currLeftNode.`val`
                }
                
                while(currLeftNode.right != null && currLeftNode.right != node) {
                    currLeftNode = currLeftNode.right
                }
                
                if(currLeftNode.right == null) {
                    currLeftNode.right = node
                    node = node.left
                } else {
                    // means it has already a link
                    currLeftNode.right = null
                    if(node.right != null) {
                        node = node.right
                    } else {
                        break
                    }
                }
            }
        }
        
        return total
    }
}

// 38. Two Sum
class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var first: Int = 0
        var second: Int = 0
        
        val ht = HashMap<Int, Int>()
        
        for(i in 0 until nums.size) {
            val diff: Int = target - nums[i]
            if(ht.containsKey(diff)) {
                first = i
                second = ht[diff]!!
                break
            } else {
                val currValue = nums[i]
                ht.put(currValue, i)
            }
        }
        return intArrayOf(first, second)
    }
}

// 39. Valid Palindrome
class Solution {
    // 1. remove non-alphanumeric 2. remove whitespaces 3. lowercase
    
    // recursive
    fun isPalindrome(s: String): Boolean {
        val preprocessesList: List<Char> = preprocess(s)

        return mainAction(preprocessesList)
    }
        
    fun mainAction(preprocessesList: List<Char>): Boolean {
        if (preprocessesList.size == 0 || preprocessesList.size == 1) {
            return true
        } else if (preprocessesList.size == 2) {
            return preprocessesList[0] == preprocessesList[1]
        } else {
            if (preprocessesList.first() == preprocessesList.last()) {
                return mainAction(
                    preprocessesList.subList(1, preprocessesList.size-1)
                )
            } else {
                return false
            }
        }
        
    }
    
    fun preprocess(currStr: String): List<Char> {
        val filteredList: List<Char> = currStr
            .filterNot { it.isWhitespace() }
            .filter { it.isLetterOrDigit() }
            .toList()
        
        val resultList: List<Char> = filteredList.map { it.toLowerCase() }
        
        return resultList
    }
    
    // iterative
    fun isPalindrome(s: String): Boolean {
        val preprocessedList: List<Char> = preprocess(s)
        
        var i: Int = 0
        var j: Int = preprocessedList.size - 1
        
        while(i <= j) {
            val leftChar: Char = preprocessedList[i]
            val rightChar: Char = preprocessedList[j]
            
            if (leftChar != rightChar) {
                return false
            }
            i += 1
            j -= 1
        }
        
        return true
    }
    
    
    fun preprocess(currString: String): List<Char> {
        val filteredList: List<Char> = currString
            .filterNot { it.isWhitespace() }
            .filter { it.isLetterOrDigit() }
            .toList()
            .map { it.toLowerCase() }
        
        return filteredList
    }
}

// 40. Can Place Flowers
class Solution {
    // O(n) Ordinary
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        var count: Int = 0

        for(i in 0 until flowerbed.size) {
            if(flowerbed[i] == 0) {
                if(i == 0 || flowerbed[i-1] == 0) {
                    if(i == flowerbed.size-1 || flowerbed[i+1] == 0) {
                        flowerbed[i] = 1
                        count += 1
                    }
                } else {
                    continue // i != 0 AND i-1 is already 1
                }
            } else {
                continue // no need to check as already 1
            }
        }

        return count >= n
    }

    // O(n) Optimized
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        var count: Int = 0

        for(i in 0 until flowerbed.size) {
            if(flowerbed[i] == 0) {
                if(i == 0 || flowerbed[i-1] == 0) {
                    if(i == flowerbed.size-1 || flowerbed[i+1] == 0) {
                        flowerbed[i] = 1
                        count += 1
                    }
                }
            }

            if(count >= n) {
                return true
            }
        }

        return false
    }
}

// 41. Symmetric Tree
class Solution {
    fun isSymmetric(root: TreeNode?): Boolean {
        if(root == null) {
            return true
        }
        return checkIsSymmetric(root.left, root.right)
    }

    fun checkIsSymmetric(leftTree: TreeNode?, rightTree: TreeNode?): Boolean {
        if(leftTree == null && rightTree == null) {
            return true
        } else if((leftTree == null || rightTree == null) ||
            leftTree.`val` != rightTree.`val`) {
            return false
        } else {
            return checkIsSymmetric(leftTree.left, rightTree.right) &&
                    checkIsSymmetric(leftTree.right, rightTree.left)
        }
    }
}

// 42. Plus One
class Solution {
    fun plusOne(digits: IntArray): IntArray {
        var allDigits: MutableList<Int> = digits.toMutableList()
        val length: Int = digits.size
        
        for(i in 0 until length) {
            var idx: Int = length - i - 1
            
            if(allDigits[idx] == 9) {
                allDigits[idx] = 0
            } else {
                allDigits[idx] = allDigits[idx] + 1
                return allDigits.toIntArray()
            }
        }
        
        allDigits.add(0, 1)
        return allDigits.toIntArray()
    }
}


// 43. Move Zeroes
class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var j: Int = 0
        var i: Int = 0
        
        while (j < nums.size) {
            while (j < nums.size && nums[j] == 0) {
                j += 1
            }
            
            if(j > nums.size - 1) {
                break
            }
            
            if(nums[i] == 0) {
                swap(i, j, nums)
            }
            
            i += 1
            j += 1
        }
    }
    
    fun swap(i: Int, j: Int, nums: IntArray): Unit {
        val firstVal: Int = nums[i]
        val secondVal: Int = nums[j]
        
        nums[j] = firstVal
        nums[i] = secondVal
    }
}

// 44. Find All Numbers Disappeared in an Array
import kotlin.math.*

class Solution {    
    // O(n) Time & Space
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        val allNums = mutableMapOf<Int,Boolean>()
        var result = mutableListOf<Int>()
        
        for(num in nums) {
            allNums.put(num, true)
        }
        // `until` is exclusive, hence it goes 0,1 in [1,1], but we need 2 as well
        for(i in 1 until nums.size + 1) {
            if(!allNums.containsKey(i)) {
                result.add(i)
            }
        }
        
        return result
    }
    
    // O(n) Time O(1) Space
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        for(num in nums) {
            if(nums[abs(num) - 1] > 0) {
                nums[abs(num) - 1] *= -1
            }
        }
        
        val returnList = mutableListOf<Int>()
        for(i in 0 until nums.size) {
            // as from [1,n] we need to add 1
            if(nums[i] > 0) {
                returnList.add(i + 1)
            }
        }
        
        return returnList
    }
}

// 45. Squares of a Sorted Array
import kotlin.math.*

class Solution {
    // brute force. Time O(n*log n)
    fun sortedSquares(nums: IntArray): IntArray {
        for(i in 0 until nums.size) {
            nums[i] = nums[i] * nums[i]
        }
        
        nums.sort()
        
        return nums
    }
    
    // Optimal: O(n) Time & Space
    fun sortedSquares(nums: IntArray): IntArray {
        var left: Int = 0
        var right: Int = nums.size - 1
        var finalNums = IntArray(nums.size)
        
        for(i in nums.lastIndex downTo 0) {
            val leftVal: Int = nums[left]
            val rightVal: Int = nums[right]
            
            if(abs(leftVal) > abs(rightVal)) {
                finalNums[i] = leftVal * leftVal
                left += 1
            } else {
                finalNums[i] = rightVal * rightVal
                right -= 1
            }
        }
        
        return finalNums
    }
}

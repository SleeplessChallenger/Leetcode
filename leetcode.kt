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

// 46. Invert Binary Tree
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
    fun invertTree(root: TreeNode?): TreeNode? {
        if (root == null) {
            return null
        }
        swap(root)
        
        invertTree(root.left)
        invertTree(root.right)
        
        return root
    }
    
    fun swap(node: TreeNode?): Unit {
        val nodeLeft: TreeNode? = node!!.left
        val nodeRight: TreeNode? = node!!.right
        
        node.left = nodeRight
        node.right = nodeLeft
    }
    
    // iterative
    fun invertTree(root: TreeNode?): TreeNode? {
        var queue = mutableListOf<TreeNode?>(root)
        
        while(queue.size != 0) {
            val currNode: TreeNode? = queue.removeAt(0)
            
            if (currNode == null) {
                continue
            }
            
            swap(currNode)
            
            queue.add(currNode.left)
            queue.add(currNode.right)
        }
        
        return root
    }
}

// 47. Kth Largest Element in a Stream
class KthLargest(k: Int, nums: IntArray) {
    // in `siftUp()` use `var idx` instead of `val` otherwise change doesn't happen

    // heap
    var currNums = MinHeap(nums.toMutableList())
    val checkMark: Int = k

    fun add(`val`: Int): Int {
        currNums.insert(`val`)

        var toRemoveCount = currNums.checkLength() - checkMark

        // if (toRemoveCount > 0) {
        //     repeat(toRemoveCount) {
        //         currNums.delete()
        //     }
        // }
        
        while(toRemoveCount != 0) {
            currNums.delete()
            toRemoveCount -= 1
        }

        return currNums.peek()
    }
}

class MinHeap(arr: MutableList<Int>) {

    val heap: MutableList<Int> = createHeap(arr)

    fun createHeap(arr: MutableList<Int>): MutableList<Int> {
        val parentIdx = (arr.size - 2) / 2
        for(i in parentIdx downTo 0) {
            siftDown(i, arr.size - 1, arr)
        }

        return arr
    }

    fun insert(value: Int): Unit {
        heap.add(value)
        siftUp()
    }

    fun checkLength() = heap.size

    fun siftUp(): Unit {
        var idx = checkLength() - 1
        
        while(idx > 0) {
            val parentIdx = (idx - 1) / 2

            if(heap[idx] < heap[parentIdx]) {
                swap(heap, idx, parentIdx)
                idx = parentIdx
            } else {
                return
            }
        }
    }

    fun siftDown(idx: Int, length: Int, heap: MutableList<Int>): Unit {
        var newIdx: Int = idx
        
        var idxOne = newIdx * 2 + 1
        
        while(idxOne <= length) {
            var idxTwo = when {
                newIdx * 2 + 2 <= length -> {
                    newIdx * 2 + 2
                } else -> {
                    -1
                }
            }

            val swapIdx: Int = if(idxTwo != -1 && heap[idxOne] > heap[idxTwo]) {
                idxTwo
            } else {
                idxOne
            }

            if(heap[swapIdx] < heap[newIdx]) {
                swap(heap, swapIdx, newIdx)
                newIdx = swapIdx
                idxOne = newIdx * 2 + 1
            } else {
                return
            }
        }
    }

    // it'll give -1 if our `heap` is empty
    fun peek(): Int = heap.first()

    fun delete(): Int {
        val nodeToDelete = heap[0]

        val length: Int = checkLength()
        val newHead: Int = heap.removeAt(length - 1)
        
        // val newHead = heap.removeLast()

        val currLengthHeap = checkLength()

        if(currLengthHeap > 0) {
            heap[0] = newHead
            siftDown(0, checkLength()-1, heap)
        }
        return nodeToDelete
    }

    fun swap(heap: MutableList<Int>, i: Int, j: Int): Unit {
        val valueOfi = heap[i]
        val valueOfj = heap[j]

        heap[i] = valueOfj
        heap[j] = valueOfi
    }
}

//     brute-froce with sorting
    var currNums = nums.toMutableList()
    val currK = k
    
    fun add(`val`: Int): Int {
        currNums.add(`val`)
        
        currNums.sort()
        return currNums[currNums.size-currK]
    }


// paritioning
class KthLargest(k: Int, nums: IntArray) {
    
    var valList: MutableList<Int> = nums.toMutableList()
    val kCheck: Int = k
    
    fun add(`val`: Int): Int {
        valList.add(`val`)
        
        var j: Int = 0
        var lastIdx: Int = valList.size - 1
        
        while(j <= lastIdx) {
            val pivotIdx: Int = (j..lastIdx).random()
            
            val curr_pivot_idx = doPartition(valList, j, lastIdx, pivotIdx)
            
            if(curr_pivot_idx == (valList.size - kCheck)) {
                return valList[curr_pivot_idx]
            } else if((valList.size - kCheck) > curr_pivot_idx) {
                j = curr_pivot_idx + 1
            } else if(((valList.size - kCheck)) < curr_pivot_idx) {
                lastIdx = curr_pivot_idx - 1
            }
        }
        
        return -1
    }
    
    fun doPartition(valList: MutableList<Int>, j: Int, lastIdx: Int, pivotIdx: Int): Int {
        val pivotValue: Int = valList[pivotIdx]
        
        swap(valList, pivotIdx, lastIdx)
        
        var leftBorder: Int = j
        var movingIdx: Int = j

        while(movingIdx <= lastIdx) {
            if(valList[movingIdx] > pivotValue) {
                movingIdx += 1
            } else if(valList[movingIdx] < pivotValue) {
                swap(valList, movingIdx, leftBorder)
                movingIdx += 1
                leftBorder += 1
            } else {
               movingIdx += 1 
            }
        }
        
        swap(valList, lastIdx, leftBorder)
        return leftBorder
    }
    
    fun swap(valList: MutableList<Int>, i: Int, j: Int): Unit {
        val firstVal: Int = valList[i]
        val secondVal: Int = valList[j]
        
        valList[i] = secondVal
        valList[j] = firstVal
    }
}

// 48. Valid Mountain Array
class Solution {
    fun validMountainArray(arr: IntArray): Boolean {
        val length: Int = arr.size
        
        if (arr.size < 3) {
            return false
        }
        
        var idx: Int = 0
        
        while (idx + 1 < length && arr[idx] < arr[idx+1]) {
            idx += 1
        }
        
        if (idx == 0 || idx == length - 1) { // -1 is crucial as we want to check whether we reach last idx or not. Why? => last means either monotonic or strict increase
            return false
        }
        
        while (idx + 1 < length && arr[idx] > arr[idx+1]) {
            idx += 1
        }
        
        return idx == length - 1
        // what's this? => we cam stop traverse when last - 1 < last, but that's wrong and hence we need to verify: we reach LAST idx
    }
}

// 49. Missing Number
class Solution {
    // O(n) Time O(n) Space
    fun missingNumber(nums: IntArray): Int {
        val hashTable = mutableMapOf<Int, Boolean>()
        for(num in nums) {
            hashTable.put(num, true)
        }
        
        var returnKey: Int = 0
        
        for(i in 0 until nums.size + 1) {
            if(!hashTable.containsKey(i)) {
                returnKey = i
                break
            }
        }
        
        return returnKey
    }
    
    // O(n * log n) Time O(1) Space
    fun missingNumber(nums: IntArray): Int {
        nums.sort()
        
        if(nums[0] != 0) {
            return 0
        }
        
        for(i in 1 until nums.size) {
            val currNum: Int = nums[i]
            val prevNum: Int = nums[i-1]

            if (currNum - prevNum > 1) {
                return prevNum + 1
            }
        }

        return nums.last() + 1
    }
    
    // O(n) Time O(1) Space
    fun missingNumber(nums: IntArray): Int {
        // don't use `numsLength` in loop as it'll change
        var numsLength: Int = nums.size
        
        for(i in 0 until nums.size) {
            val num: Int = nums[i]
            val bit = num xor i
            numsLength = bit xor numsLength
        }
        
        return numsLength
    }
}

// 50. Best Time to Buy and Sell Stock
class Solution {
    fun maxProfit(prices: IntArray): Int {
        if (prices.size <= 1) {
            return 0
        }
        
        var minValue: Int = Int.MAX_VALUE
        var currMax: Int = 0
        
        for (i in 0 until prices.size) {
            val curr: Int = prices[i]
            
            if (curr < minValue) {
                minValue = curr
                continue
            } else {
                if (currMax > curr - minValue) {
                    continue
                } else {
                    currMax = curr - minValue
                }
            }
        }

        return currMax
    }
} 

// If we use both max & min: issue is that max may stay the same, but min will change
// and we result in `min` idx being further than `max` idx
// [7,6,4,3,1]

// 51. Validate Binary Search Tree
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

//52. Majority Element
class Solution {
    // hashtable
    fun majorityElement(nums: IntArray): Int {
        val hashtable = mutableMapOf<Int,Int>()
        
        for(num in nums) {
            if (!hashtable.containsKey(num)) {
                hashtable[num] = 1
            } else {
                hashtable[num] = hashtable[num]!! + 1
            }
        }
        
        val maxKey: Int = hashtable
                .maxBy { it.value }!!
                .key

        return maxKey
    }
    
    // O(1) Space
    fun majorityElement(nums: IntArray): Int {
        var count: Int = 0
        var candidate: Int = 0
        
        for(num in nums) {
            if (count == 0) {
                candidate = num
            }
            count = when {
                candidate == num -> {
                    count + 1
                } else -> {
                    count - 1
                }
            }
        }
        
        return candidate
    }
    
    // Divide & Conquer
    fun majorityElement(nums: IntArray): Int {
        return findMajorElement(nums, 0, nums.size-1)
    }
    
    fun findMajorElement(nums: IntArray, lo: Int, hi: Int): Int {
        if (lo == hi) {
            return nums[lo]
        }
        
        val mid: Int = lo + (hi - lo) / 2
        
        val left = findMajorElement(nums, lo, mid)
        val right = findMajorElement(nums, mid+1, hi)
        
        if (left == right) {
            return left
        }
        
        val leftCount: Int = countNums(nums, left)
        val rightCount: Int = countNums(nums, right)
        
        val result: Int = if (leftCount > rightCount) left else right
        return result
        
    }
    
    fun countNums(nums: IntArray, target: Int): Int {
        var count: Int = 0
        
        for(num in nums) {
            if (num == target) {
                count += 1
            }
        }
        
        return count
    }
}

// 53. Convert Sorted Array to Binary Search Tree
class Solution {
    fun sortedArrayToBST(nums: IntArray): TreeNode? {
        return createTree(nums, 0, nums.size - 1)
    }
    
    fun createTree(nums: IntArray, lo: Int, hi: Int): TreeNode? {
        if (lo > hi) {
            return null
        }
        
        val midIdx: Int = lo + (hi - lo)/2
        val node: TreeNode = TreeNode(nums[midIdx])
        // Why +1/-1? => We need to omit current index
        node.left = createTree(nums, lo, midIdx - 1)
        node.right = createTree(nums, midIdx + 1, hi)
        
        return node
    }
}

// 54. Split Array Largest Sum
import kotlin.math.*

class Solution {
    fun splitArray(nums: IntArray, m: Int): Int {
        var left: Int = nums.max()!!
        var right: Int = nums.sum()
        
        var result: Int = 0
        
        while (left <= right) {
            var guessValue: Int = left + (right - left) / 2
            val splitsRequired: Int = findMinSplits(nums, guessValue)
            
            if (splitsRequired <= m) {
                right = guessValue - 1
                result = guessValue
            } else {
                left = guessValue + 1
            }
        }
        
        return result
    }
    
    fun findMinSplits(nums: IntArray, guessValue: Int): Int {
        var splits: Int = 0
        var currSum: Int = 0
        
        for(num in nums) {
            if (currSum + num <= guessValue) {
                currSum += num
            } else {
                currSum = num
                splits += 1
            }
        }
        return splits + 1
    }
}

// 55. Reverse Linked List
class Solution {
    fun reverseList(head: ListNode?): ListNode? {
        var currNode: ListNode? = head
        var nextNode: ListNode? = null
        var prevNode: ListNode? = null

        while (currNode != null) {
            nextNode = currNode.next // save next node
            currNode.next = prevNode // reverse link
            prevNode = currNode
            currNode = nextNode
        }

        return prevNode
    }
}

// 56. Two Sum II - Input Array Is Sorted
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

    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var left: Int = 0
        var right: Int = numbers.size - 1

        var res1: Int = 0
        var res2: Int = 0

        while (left <= right) {
            val sumOfTwo: Int = numbers[left] + numbers[right]

            if (sumOfTwo == target) {
                res1 = left + 1
                res2 = right + 1
                break
            } else if (sumOfTwo > target) {
                right -= 1
            } else {
                left += 1
            }
        }

        return intArrayOf(res1, res2)
    }
}

// 57. Contains Duplicate III
// Time: n*log min(n,k); Space: min(n,k)
class Solution {
    fun containsNearbyAlmostDuplicate(nums: IntArray, k: Int, t: Int): Boolean {
       var treeSet = TreeSet<Long>()
       
       for(i in 0 until nums.size) {
           // floor is MAX that is SMALLER than current
           val floor: Long? = treeSet.floor(nums[i].toLong())
           
           if(floor != null && nums[i] - floor <= t) {
               return true
           }
           // ceil is MIN that is BIGGER than current
           val ceil: Long? = treeSet.ceiling(nums[i].toLong())
           
           if(ceil != null && ceil - nums[i] <= t) {
               return true
           }
           
           treeSet.add(nums[i].toLong())
           
           // here we remove oldest. Why `i - k`? Because diff
           // in indicies can't be bigger than `k`. Hence, if
           // answer wasn't found with value to be removed, we
           // simply remove it.
           if(treeSet.size > k) {
               treeSet.remove(nums[i - k].toLong())
           }
       }
       
       return false
    }
}

// 58. Unique Binary Search Trees II
class Solution {
    fun generateTrees(n: Int): List<TreeNode?> {
        return this.traverseNodes(1, n)
    }
    
    fun traverseNodes(start: Int, n: Int): List<TreeNode?> {
        // base case
        if (start > n) {
            return mutableListOf(null)
        }
        
        val allNodes: MutableList<TreeNode?> = mutableListOf<TreeNode?>()
        
        for(i in start until n + 1) {
            // I can say we have 2 so-called base cases:
            // a) when we return `null` b) when we return `[node]` with .null on both sides  
            val leftPart: List<TreeNode?> = this.traverseNodes(start, i - 1)
            val rightPart: List<TreeNode?> = this.traverseNodes(i + 1, n)

            for(left in leftPart) {
                for(right in rightPart) {
                    val node: TreeNode = TreeNode(i)
                    
                    node.left = left
                    node.right = right
                    
                    allNodes.add(node)
                }
            }
        }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        return allNodes
    }
}

// 59. Find Pivot Index
class Solution {
    fun pivotIndex(nums: IntArray): Int {
        // so, `allSum - leftSum` is diff, but adding `currValue`
        // means that if `if condition` works => THIS index is pivot
        val allSum: Int = nums.sum()
        var leftSum: Int = 0
        
        for(i in 0 until nums.size) {
            val currValue: Int = nums[i]
            if(allSum - currValue - leftSum == leftSum) {
                return i
            }
            leftSum += currValue
        }
        
        return -1
    }
}

// 60. Largest Number At Least Twice of Others
class Solution {
    fun dominantIndex(nums: IntArray): Int {
        var firstIndex: Int = Int.MIN_VALUE
        var biggestVal: Int = nums.max()!!
        
        for(i in 0 until nums.size) {
            val valueNum: Int = nums[i]
            if (valueNum != biggestVal && valueNum * 2 > biggestVal) {
                return -1
            } else if (valueNum == biggestVal) {
                firstIndex = i
            }
        }
        return firstIndex
    }
}

// 61. Diagonal Traverse

// ver. 1
class Solution {
    // In Kotlin if we want to `extend` -> use `+=`
    fun findDiagonalOrder(mat: Array<IntArray>): IntArray {
        val allElements: MutableMap<Int, MutableList<Int>> = mutableMapOf<Int, MutableList<Int>>()
        
        for(i in 0 until mat.size) {
            for(j in 0 until mat[i].size) {
                val currKey: Int = i + j
                if (!allElements.containsKey(currKey)) {
                    allElements.put(currKey, mutableListOf(mat[i][j]))
                } else {
                    allElements[currKey]!! += (mutableListOf(mat[i][j]))
                }
            }
        }
        
        val result: MutableList<Int> = mutableListOf<Int>()

        for((k, v) in allElements) {
            if (k % 2 == 0) {
                result += this.reverseList(v) // here we need to reverse
            } else {
                result += v // TODO: here we need to merge and nothing more
            }
        }
        return result.toIntArray()
    }
    
    fun reverseList(currList: MutableList<Int>): MutableList<Int> {
        return currList.asReversed()
    }
}

// ver. 2
class Solution {
    fun findDiagonalOrder(mat: Array<IntArray>): IntArray {
        val height: Int = mat.size
        val width: Int = mat[0].size
        
        val result: MutableList<Int> = mutableListOf<Int>()
        val tempResult: MutableList<Int> = mutableListOf<Int>()
        
        for(idx in 0 until (height + width - 1)) {
            tempResult.clear()
            
            var row = when {
                idx < width -> {
                    0
                } else -> {
                    idx - width + 1
                }
            }
            
            var col = when {
                idx < width -> {
                    idx
                } else -> {
                    width - 1
                }
            }
            
            while (row < height && col > -1) {
                tempResult.add(mat[row][col])
                row += 1
                col -= 1
            }
            
            if (idx % 2 == 0) {
                // as we start from 0, 0 is odd and 1 is even
                result += tempResult.asReversed()
            } else {
                result += tempResult
            }
        }
        
        return result.toIntArray()
    }
}

// 62. Spiral Matrix
class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        var startRow: Int = 0
        var startCol: Int = 0
        var endRow: Int = matrix.size - 1
        var endCol: Int = matrix[0].size - 1
        
        val result = mutableListOf<Int>()
        
        while (startRow <= endRow && startCol <= endCol) {
            // from very start to very end
            for(i in startCol until endCol + 1) {
                result.add(matrix[startRow][i])
            }
            
            // from one further to very end
            for(i in startRow + 1 until endRow + 1) {
                result.add(matrix[i][endCol])
            }
            
            // from one behind to very end
            for(i in endCol - 1 downTo startCol) {
                // check
                if (startRow == endRow) {
                    break
                }
                
                result.add(matrix[endRow][i])
            }
            
            // from one behind to one further
            for(i in endRow - 1 downTo startRow + 1) {
                // check
                if (startCol == endCol) {
                    break
                }
                
                result.add(matrix[i][startCol])
            }
            
            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1
        }
        
        return result.toList()
    }
}

// 63. Array Partition I
class Solution {
    fun arrayPairSum(nums: IntArray): Int {
        var result: Int = 0
        nums.sort()
        
        for(i in 0 until nums.size step 2) {
            result += nums[i]
        }
        
        return result
    }
}

// 64. Remove Element
class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        // 1. use 2 pointers: fast & slow runners
        // 2. if fast != v: move it, else swap and move booth        
        var slow: Int = 0
        var fast: Int = 1
        
        if (nums.size == 1) {
            // because if [2] 3, we need index of 1 as we need next after ours
            return if (nums[0] == `val`) slow else slow + 1
        }
        if (nums.size == 0) {
            return 0
        }
        
        while (fast < nums.size) {
            if (nums[slow] != `val`) {
                fast += 1
                slow += 1
            } else {
                if (nums[fast] != `val`) {
                    this.swap(fast, slow, nums)
                    slow += 1
                }
                fast += 1
            }
        }
        // if `slow` element == `val`, we need to return it, otherwise next element
        return if (nums[slow] == `val`) slow else slow + 1
    }
    
    fun swap(i: Int, j: Int, nums: IntArray): Unit {
        val firstVal: Int = nums[i]
        val secondVal: Int = nums[j]
        
        nums[i] = secondVal
        nums[j] = firstVal
    }
}

// 65. Max Consecutive Ones
import kotlin.math.*

class Solution {
    fun findMaxConsecutiveOnes(nums: IntArray): Int {
        if (nums.size == 1) {
            return if (nums[0] == 1) 1 else 0
        }
        
        var currOnes: Int = 0
        var maxOnes: Int = 0
        
        for(num in nums) {
            if (num == 1) {
                currOnes += 1
                maxOnes = max(currOnes, maxOnes)
            } else {
                currOnes = 0   
            }
        }
        
        return maxOnes
    }
}

// 66. Pascal's Triangle II
class Solution {
    fun getRow(rowIndex: Int): List<Int> {
        val result: MutableList<MutableList<Int>> = 
            mutableListOf<MutableList<Int>>(mutableListOf<Int>(1))
        
        for(i in 1 until rowIndex + 1) {
            val currList: MutableList<Int> = mutableListOf<Int>(1)
            
            for(j in 1 until i) {
                val firstVal: Int = result[i-1][j-1]
                val secondVal: Int = result[i-1][j]
                
                currList.add(firstVal + secondVal)
            }
            
            currList.add(1)
            result += currList
        }
        
        return result[rowIndex]
    }
}

// 67. Minimum Size Subarray Sum
import kotlin.math.*

class Solution {
    fun minSubArrayLen(target: Int, nums: IntArray): Int {
        var answer: Int = Int.MAX_VALUE
        var left: Int = 0
        var sum: Int = 0
        
        for(idx in 0 until nums.size) {
            sum += nums[idx]
            
            while (sum >= target) {
            // + 1 as indicies start from 0, hence to find the length we need to add 1
                answer = min(answer, idx + 1 - left)
                sum -= nums[left]
                left += 1
            }
        }
        
        return if (answer == Int.MAX_VALUE) 0 else answer
    }
}

// 68. Rotate Array
class Solution {
    // O(n) time & space
    fun rotate(nums: IntArray, k: Int): Unit {
        val tempArray = MutableList<Int>(nums.size) { 0 }
        for(i in 0 until nums.size) {
            val newIdx: Int = (i + k) % nums.size
            tempArray[newIdx] = nums[i]
        }
        
        for(i in 0 until nums.size) {
            nums[i] = tempArray[i]
        }
    }
    
    // O(n) Time & O(1) Space
    fun rotate(nums: IntArray, k: Int): Unit {
        fun reverse(start: Int, end: Int): Unit {
            var i: Int = start
            var j: Int = end
            
            while (i < j) {
                val leftVal: Int = nums[i]
                val rightVal: Int = nums[j]
                
                nums[i] = rightVal
                nums[j] = leftVal
                
                i += 1
                j -= 1
            }
        }
        val length: Int = nums.size
        val idx: Int = k % length
        
        reverse(0, length - 1)
        reverse(0, idx - 1)
        reverse(idx, length - 1)
    }
}

// 69. Implement strStr()
class Solution {
    fun strStr(haystack: String, needle: String): Int {
        if (haystack.length == 0 && needle.length == 0) {
            return 0
        } else if (haystack.length != 0 && needle.length == 0) {
            return 0
        } else {
            val pattern = this.makePattern(needle)
            return this.findSize(pattern, haystack, needle)
        }
    }

    fun makePattern(needle: String): MutableList<Int> {
        var i: Int = 0
        var j: Int = 1

        val pattern = MutableList<Int>(needle.length) { -1 }

        while (j < needle.length) {
            if (needle[j] == needle[i]) {
                pattern[j] = i
                i += 1
                j += 1
            } else if (i > 0) {
                i = pattern[i-1] + 1
            } else {
                j += 1
            }
        }

        return pattern
    }

    fun findSize(pattern: MutableList<Int>, bigString: String, smallString: String): Int {
        var i: Int = 0
        var j: Int = 0
        // current index from big string + len of small string - current index of small string
        while (j + smallString.length - i <= bigString.length) {
            if (smallString[i] == bigString[j]) {
                if (i == smallString.length - 1) {
                    return j - i
                }
                i += 1
                j += 1
            } else if (i > 0) {
                i = pattern[i-1] + 1
            } else {
                j += 1
            }
        }
        return -1
    }
}

// 70. Reverse Words in a String
class Solution {
    fun reverseWords(s: String): String {
        // 1. strip() left & right ends
        // 2. make upper loop to traverse whole string
        // 3. if current letter is " " & word() array != [] -> push left
        // 4. if current letter != " " -> append to word() array
        var left: Int = 0
        var right: Int = s.length - 1

        while (left <= right && s[left].isWhitespace()) {
            left += 1
        }

        while (left <= right && s[right].isWhitespace()) {
            right -= 1
        }

        var finalResult = mutableListOf<String>()
        val words = mutableListOf<Char>()

        while (left <= right) {
            val currentLetter = s[left]

            if (currentLetter.isWhitespace() && (words.size != 0)) {
                finalResult.add(0, words.joinToString(""))
                words.clear()
            } else if (!currentLetter.isWhitespace()) {
                words.add(currentLetter)
            } // if space && words == 0 -> skip to bypass multiple " "

            left += 1
        }

        finalResult.add(0, words.joinToString(""))
        return finalResult.joinToString(" ")
    }
}

// 71. Reverse Words in a String III
class Solution {
    fun reverseWords(s: String): String {
        var allWords = mutableListOf<Char>()

        for(token in s) {
            allWords.add(token)
        }

        var runningIdx: Int = 0
        var start: Int = 0
        val length: Int = s.length

        while (runningIdx < length) {
            while (runningIdx < length && !allWords[runningIdx].isWhitespace()) {
                runningIdx += 1
            }

            this.reverseTokens(allWords, start, runningIdx-1)

            runningIdx += 1
            start = runningIdx
        }

        this.reverseTokens(allWords, start, runningIdx-1)

        return allWords.joinToString("")
    }

    fun reverseTokens(allWords: MutableList<Char>, start: Int, end: Int): Unit {
        var i: Int = start
        var j: Int = end

        while (i < j) {
            val firstToken: Char = allWords[i]
            val secondToken: Char = allWords[j]

            allWords[i] = secondToken
            allWords[j] = firstToken

            i += 1
            j -= 1
        }
    }
}

// 72. Remove Duplicates from Sorted Array
class Solution {
    // by using `+1`, we'll move duplicate things till the end
    fun removeDuplicates(nums: IntArray): Int {
        if (nums.size < 2) {
            return 1
        }

        var i: Int = 0
        var j: Int = 1
        val length: Int = nums.size

        while (j < length) {
            if (nums[j] == nums[i]) {
                j += 1
            } else {
                this.swap(nums, i + 1, j)
                i += 1
                j += 1
            }
        }

        return i + 1
    }

    fun swap(nums: IntArray, i: Int, j: Int): Unit {
        val firstVal = nums[i]
        val secondVal = nums[j]

        nums[i] = secondVal
        nums[j] = firstVal
    }
}

// 73. Longest Common Prefix
import kotlin.math.*

class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        if (strs.size == 0) {
            return ""
        }
        
        var prefix: String = strs[0]

        for(i in 1 until strs.size) {
            val currWord: String = strs[i]

            while (!currWord.startsWith(prefix)) {
                val prefixLength: Int = prefix.length
                // `untils` is exclusive, but `prefixLength` is length. Recall indicies stuff
                prefix = prefix.slice(0 until prefixLength - 1)
            }
        }
        
        return prefix
    }
    
    // !! Below has some error
    // Divide & Conquer
    fun longestCommonPrefix(strs: Array<String>): String {
        if (strs.size == 1) {
            return strs[0]
        }
        val result = this.dividePart(strs, 0, strs.size-1)
        return result
    }
    
    fun dividePart(strs: Array<String>, lo: Int, hi: Int): String {
        // 1. We take all left and rec till one left
        // 2. On the right we always have 1 left
        // 3. Then we take 1 left & 1 right: process them
        //     => return one result which is common prefix to `left_result` as `right_result` always keeps one
        if (lo == hi) {
            return strs[lo]
        }
                
        val mid: Int = (lo + hi) / 2
        
        val leftResult: String = this.dividePart(strs, lo, mid)
        val rightResult: String = this.dividePart(strs, mid+1, hi)
        
        return this.conquerPart(leftResult, rightResult)
    }
    
    fun conquerPart(leftResult: String, rightResult: String): String {
        val smallestInt: Int = min(leftResult.length, rightResult.length)
        
        for(i in 0 until smallestInt) {
            if (leftResult[i] != rightResult[i]) {
                return leftResult.substring(0..i)
            }
        }
        
        return leftResult.substring(0..smallestInt)
    }
}

// 74. Add Binary
import kotlin.math.*

class Solution {
    fun addBinary(a: String, b: String): String {
        val length: Int = max(a.length, b.length)
        
        var currA = a.padStart(length, '0')
        var currB = b.padStart(length, '0')

        var carry: Int = 0
        val result = mutableListOf<Char>()
        
        for(i in (length - 1) downTo 0) {
            if (currA[i] == '1') {
                carry += 1
            }
            if (currB[i] == '1') {
                carry += 1
            }
            
            if (carry % 2 == 1) {
                result.add('1')
            } else {
                result.add('0')
            }
            
            carry /= 2

        }

        if (carry == 1) {
            result.add('1')
        }
        
        val finalAnswer = result.reversed()
        
        return finalAnswer.joinToString("")
    }
}

// 75. Design HashSet
class MyHashSet {
    private val primaryKey: Int = 769
    private val bucket = this.createBuckets()

    private fun createBuckets(): ArrayList<LLBucket> {
        val bucket = arrayListOf<LLBucket>()

        for(i in 0 until this.primaryKey) {
            bucket.add(LLBucket())
        }

        return bucket
    }

    private fun hashFunction(value: Int): Int {
        return value % this.primaryKey
    }

    fun add(key: Int): Unit {
        val bucketIndex: Int = this.hashFunction(key)
        bucket[bucketIndex].insert(key)
        return
    }

    fun remove(key: Int): Unit {
        val bucketIndex: Int = this.hashFunction(key)
        bucket[bucketIndex].remove(key)
    }

    fun contains(key: Int): Boolean {
        val bucketIndex: Int = this.hashFunction(key)
        return bucket[bucketIndex].exist(key)
    }

}

data class Node constructor(val value: Int, var next: Node? = null)

class LLBucket {
    private val head: Node = Node(0)

    fun insert(value: Int) {
       if (!this.exist(value)) {
           val newNode: Node = Node(value, this.head.next)
           head.next = newNode
       }
    }

    fun remove(value: Int) {
        var prevNode = this.head
        var currNode = this.head.next

        while (currNode != null) {
            if (currNode.value == value) {
                prevNode.next = currNode.next
                return
            }

            prevNode = currNode
            currNode = currNode.next
        }
    }

    fun exist(value: Int): Boolean {
        var currNode = this.head.next

        while (currNode != null) {
            if (currNode!!.value == value) {
                return true
            }
            currNode = currNode!!.next
        }
        return false
    }
}

// 76. Design HashMap
class MyHashMap {
    private fun createBucket(): ArrayList<Bucket> {
        val bucket = arrayListOf<Bucket>()

        for(i in 0 until this.primeNum) {
            bucket.add(Bucket())
        }

        return bucket
    }

    private val primeNum: Int = 2069
    private val bucket = this.createBucket()

    private fun hashFunction(key: Int): Int {
        return key % this.primeNum
    }

    fun put(key: Int, value: Int): Unit {
        val bucketIndex: Int = this.hashFunction(key)
        this.bucket[bucketIndex].add(key, value)
    }

    fun get(key: Int): Int {
        val bucketIndex: Int = this.hashFunction(key)
        return this.bucket[bucketIndex].contains(key)
    }

    fun remove(key: Int): Unit {
        val bucketIndex: Int = this.hashFunction(key)
        this.bucket[bucketIndex].delete(key)
    }
}

class Bucket {
    private val bucket = arrayListOf<Pair<Int, Int>>()

    fun add(key: Int, value: Int): Unit {
        var flag: Boolean = false

        for(i in 0 until bucket.size) {
            val currPair: Pair<Int, Int> = bucket[i]
            val (existingKey: Int, _: Int) = currPair

            if (existingKey == key) {
                bucket[i] = Pair(existingKey, value)
                flag = true
                break
            }
        }

        if (!flag) {
            this.bucket.add(Pair(key, value))
        }

        return
    }

    fun contains(key: Int): Int {
        for (currPair in this.bucket) {
            val (existingKey: Int, existingValue: Int) = currPair
            if (existingKey == key) {
                return existingValue
            }
        }

        return -1
    }

    fun delete(key: Int): Unit {
        for(currPair in this.bucket) {
            val (existingKey: Int, _: Int) = currPair
            if (existingKey == key) {
                this.bucket.remove(currPair)
                break
            }
        }

        return
    }
}

// 77. Single Number
class Solution {
    // ver. 1
    fun singleNumber(nums: IntArray): Int {
        val ht = mutableMapOf<Int, Int>()
        for (num in nums) {
            if (!ht.containsKey(num)) {
                ht.put(num, 0)
            }
            ht[num] = ht[num]!! + 1
        }
        
        var result: Int = 0
        for((k,v) in ht) {
            if (v == 1) {
                result = k
                break
            }
        }
        
        return result
    }
    
    // ver. 2
    fun singleNumber(nums: IntArray): Int {
        var result: Int = 0
        for(num in nums) {
            result = result xor num
        }
        
        return result
    }
}

// 78. Intersection of Two Arrays
class Solution {
    using hash table
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        val firstHashTable = mutableMapOf<Int, Boolean>()
        val secondHashTable = mutableMapOf<Int, Boolean>()
        
        for(num in nums1) {
            firstHashTable.put(num, true)
        }
        
        for(num in nums2) {
            secondHashTable.put(num, true)
        }
        
        val result = mutableListOf<Int>()
        
        for((k,v) in firstHashTable) {
            if (secondHashTable.contains(k)) {
                result.add(k)
            }
        }
        
        return result.toIntArray()
    }
    
    // using intersect
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        return nums1.intersect(nums2.toList()).toIntArray()
    }
}

// 79. Intersection of Two Arrays
class Solution {
    using hash table
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        val firstHashTable = mutableMapOf<Int, Boolean>()
        val secondHashTable = mutableMapOf<Int, Boolean>()
        
        for(num in nums1) {
            firstHashTable.put(num, true)
        }
        
        for(num in nums2) {
            secondHashTable.put(num, true)
        }
        
        val result = mutableListOf<Int>()
        
        for((k,v) in firstHashTable) {
            if (secondHashTable.contains(k)) {
                result.add(k)
            }
        }
        
        return result.toIntArray()
    }
    
    // using intersect
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        return nums1.intersect(nums2.toList()).toIntArray()
    }
}

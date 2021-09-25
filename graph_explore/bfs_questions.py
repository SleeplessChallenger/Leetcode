# 1. Find if Path Exists in Graph
class Solution:
	    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        queue = [start]
        graph = {}
        for vertex in range(n):
            graph[vertex] = []
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = {start}
        
        while len(queue) != 0:
            node = queue.pop(0)
            if node == end:
                return True
            
            for vertex in graph[node]:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)
        
        return False

# 2. All Paths From Source to Target
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        full_path = []
        queue = [[0]]
        
        while len(queue) != 0:
            curr_path = queue.pop(0)
            node = curr_path[-1]
            
            for vertex in graph[node]:
                '''
                If don't make .copy()/list()
                => further changes will affect
                another path
                '''
                temp = list(curr_path)
                temp.append(vertex)
                if vertex == len(graph) - 1:
                    full_path.append(temp)
                else:
                    queue.append(temp)

       	return full_path

# 3. Populating Next Right Pointers in Each Node
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        self.traverse(root, None, None)
        return root
    
    def traverse(self, node, parent, goLeft):
        if node is None:
            return 
        
        left, right = node.left, node.right
        self.traverse(left, node, True)
        
        if parent is None:
            # for root
            node.next = None
        elif goLeft:
            node.next = parent.right
        else:
            if parent.next is None:  
                node.next = None
            else:
                node.next = parent.next.left
        
        self.traverse(right, node, False)

    # bfs
    def connect(self, root: 'Node') -> 'Node':
    	'''
    	by default `.next` = None
    	'''
        if not root:
            return root
        
        curr = root
        queue = [curr]
        
        while len(queue) != 0:
            size = len(queue)
            
            for i in range(size):
                node = queue.pop(0)
                
                if i < size - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root

# 4. Shortest Path in Binary Matrix
class Solution:
    # outer loop: O(n); inner loop: O(1) as max 8 directions
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        queue = [[0, 0]]
        grid[0][0] = 1
        
        while len(queue) != 0:
            path = queue.pop(0)
            value = grid[path[0]][path[1]]
            if path[0] == len(grid) - 1 and path[1] == len(grid[0]) - 1:
                return value
            
            result = self.getAdjacent(path, grid)
            for r in result:
                row, col = r
                grid[row][col] = value + 1
                queue.append([row, col])
            
        return -1
        
    def getAdjacent(self, path, grid):
        result = []
        r, c = path
        
        if r > 0:
            if grid[r - 1][c] == 0:
                result.append([r - 1, c])

        if c > 0:
            if grid[r][c - 1] == 0:
                result.append([r, c - 1])

        if r + 1 <= len(grid) - 1:
            if grid[r + 1][c] == 0:
                result.append([r + 1, c])

        if c + 1 <= len(grid[0]) - 1:
            if grid[r][c + 1] == 0:
                result.append([r, c + 1])

        if r > 0 and c > 0:
            if grid[r - 1][c - 1] == 0:
                result.append([r - 1, c - 1])

        if r > 0 and c + 1 <= len(grid[0]) - 1:
            if grid[r - 1][c + 1] == 0:
                result.append([r - 1, c + 1])

        if r + 1 <= len(grid) - 1 and c > 0:
            if grid[r + 1][c - 1] == 0:
                result.append([r + 1, c - 1])

        if r + 1 <= len(grid) - 1 and c + 1 <= len(grid[0]) - 1:
            if grid[r + 1][c + 1] == 0:
                result.append([r + 1, c + 1])
        
        return result

# 5. N-ary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
    	if root is None:
    		return []

    	result = []
    	queue = [root]
    	while len(queue) != 0:
    		levels = []
    		# python will iterate number of
            # times which initially was
            # specified despite further changes
    		for _ in range(len(queue)):
    			node = queue.pop(0)
    			levels.append(node.val)
    			# extend will remove []
                # from .children array whilst
                # append() will keep them
    			queue += node.children
    			# or .extend()

    		result.append(levels)

    	return result

# 6. Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    	queue, fresh = self.check_rotten(grid)

    	queue.append((-1, -1))
    	minutes = -1
    	while len(queue) != 0:
    		node = queue.pop(0)
    		if node[0] == -1:
    			minutes += 1
    			if len(queue):
    				queue.append((-1, -1))
    		else:
    			if grid[node[0]][node[1]] != 2:
    				continue

    			result = self.helper(grid, node[0], node[1])

    			for r in result:
    				row, col = r
    				grid[row][col] = 2
    				queue.append((row, col))
    				fresh -= 1

    	return minutes if fresh == 0 else -1

    def helper(self, grid, r, c):
        result = []
        if r > 0:
            if grid[r - 1][c] == 1:
                result.append((r - 1, c))
        
        if c > 0:
            if grid[r][c - 1] == 1:
                result.append((r, c - 1))
        
        if r + 1 <= len(grid) - 1:
            if grid[r + 1][c] == 1:
                result.append((r + 1, c))
        
        if c + 1 <= len(grid[0]) - 1:
            if grid[r][c + 1] == 1:
                result.append((r, c + 1))
        
        return result

    def check_rotten(self, grid):
    	queue = []
    	fresh = 0
    	for i in range(len(grid)):
    		for j in range(len(grid[i])):
    			value = grid[i][j]
    			if value == 2:
    				queue.append((i, j))
    			elif value == 1:
    				fresh += 1

    	return queue, fresh

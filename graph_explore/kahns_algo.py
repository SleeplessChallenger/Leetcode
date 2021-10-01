# 1. Course Schedule II
class Solution:
	# classes
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        graph = self.createGraph(numCourses, prereqs)
        return self.findCourses(graph)
        
    def createGraph(self, n, prereqs):
        graph = CourseNode(n)
        
        for curr, prereq in prereqs:
            graph.update(curr, prereq)
        
        return graph
    
    def findCourses(self, graph):
        result = []
        
        for node in graph.verticies:
            isCycle = self.traverse(node, result, graph)
            if isCycle:
                return []
        
        return result
    
    def traverse(self, node, result, graph):
        if node.visiting:
            return True
        if node.visited:
            return False
        
        node.visiting = True
        for vertex in node.prereqs:
            isCycle = self.traverse(vertex, result, graph)
            if isCycle:
                return True
        
        result.append(node.course)
        node.visiting = False
        node.visited = True
        return False
        
        
class CourseNode:
    def __init__(self, courses):
        self.verticies = []
        self.graph = {}
        for course in range(courses):
            self.insert(course)
        
    def insert(self, course):
        node = Node(course)
        self.verticies.append(node)
        self.graph[course] = node
    
    def update(self, a, b):
        aNode = self.getNode(a)
        bNode = self.getNode(b)
        aNode.prereqs.append(bNode)
    
    def getNode(self, node):
        return self.graph[node]
        

class Node:
    def __init__(self, course):
        self.course = course
        self.prereqs = []
        self.visited = False
        self.visiting = False

    # ht
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        
        if not prereqs or len(prereqs) == 0:
            return [i for i in range(numCourses)]
        
        result = [0 for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]
        
        for prereq in prereqs:
            inDegree[prereq[0]] += 1
        
        zeroDegree = []
        for vertex in range(len(inDegree)):
            if inDegree[vertex] == 0:
                zeroDegree.append(vertex)
        
        if len(zeroDegree) == 0:
            return []
        
        idx = 0
        while len(zeroDegree) != 0:
            course = zeroDegree.pop(0)
            result[idx] = course
            idx += 1
            for prereq in prereqs:
                if prereq[1] == course:
                    inDegree[prereq[0]] -= 1
                    if inDegree[prereq[0]] == 0:
                        zeroDegree.append(prereq[0])
        
        for v in inDegree:
            if v != 0:
                return []
        
        return result

# 2. Alien Dictionary
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # not a valid edge case as
        # input can be one word
        # and also we may have 'aba' -> 'ab'
        # => simple list() + reverse() doesn't work
        
        # if len(words) < 2:
        #     return ''.join(list(reversed(words[0])))
        
        graph = {letter: [] for word in words for letter in word}
        
        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
             
            result = self.compare(prev, curr)
            if not result:
                return ""
            
            if result == 'Similar':
                continue
            
            letterA, letterB = result
            graph[letterA].append(letterB)
        
        result = []
        visited = {} # False: visited, True: visitng
        
        for letter in graph:
            if self.dfs(letter, visited, graph, result):
                return ""
        
        return ''.join(list(reversed(result)))
    
    def dfs(self, letter, visited, graph, result):
        if letter in visited:
            return visited[letter]
        
        visited[letter] = True
        
        for vertex in graph[letter]:
            if self.dfs(vertex, visited, graph, result):
                return True
        
        visited[letter] = False
        result.append(letter)
        
            
    
    def compare(self, a, b):
        min_length = min(len(a), len(b))
        
        # not simply one > the other,
        # but if first is bigger AND
        # prefix of both is similar
        if len(a) > len(b) and a[:min_length] == b[:min_length]:
            return False
        
        for i in range(min_length):
        # as we may face errors otherwise
            letA = a[i]
            letB = b[i]
            
            if letA != letB:
                return [letA, letB]
        
        return 'Similar'

# 3. Minimum Height Trees
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        1. find such nodes that are overall close to
            all the other nodes. Ex: leaf nodes are
            peripheral and root is centoid.
            
            !! For tree-like graph - max 2 centroids. If number
            of verticies is even - 2 centroids at max. If number
            of verticies is odd - 1 centroid at max.
        
        2. Image there're more than 2 centroids => cycles
            which contradicts our condition.
        
        3. Trim out from outer level (leaf nodes) to inner
            level till there're 2 nodes left => centroids
        '''
        if n <= 2:
            return [i for i in range(n)]
        
        graph = [[] for _ in range(n)]
        
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        queue = []
        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)
        
        count = n
        while count > 2:
            # cannot len(graph) as we don't
            # remove keys, only pop() from values
            temp = []
            count -= len(queue)
            
            while len(queue) != 0:
                node = queue.pop(0)
                
                adjacent = graph[node].pop(0)
                graph[adjacent].remove(node)
                # 2 above pop() from graph
                
                if len(graph[adjacent]) == 1:
                    temp.append(adjacent)
            
            queue = temp
        
        return queue

# 4. Parallel Courses
# with class
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        '''
        1. create graph and populate with prereqs
        2. Don't forget to increase +1 as we have
            from 1 to n, not 0 to n - 1
        '''
        graph = self.createGraph(n, relations)
        return self.findCount(graph)
    
    def createGraph(self, n, relations):
        graph = CourseClass(n)
        
        for curr, depend in relations:
            graph.addVertex(curr, depend)
        
        return graph
    
    def findCount(self, graph):
        nodes_start = list(filter(
            lambda x: x.prepreqsCount == 0,
            graph.verticies
        ))
        
        count = 0
        temp = []
        
        while len(nodes_start) != 0:
            node = nodes_start.pop(0)
            self.remove_depend(node, temp)
            
            if not len(nodes_start):
                nodes_start = temp
                temp = []
                count += 1
        
        wrong_result = any(x.prepreqsCount for x in graph.verticies)
        return -1 if wrong_result else count
    
    def remove_depend(self, node, temp):
        while len(node.depends) != 0:
            vertex = node.depends.pop(0)
            vertex.prepreqsCount -= 1
            if vertex.prepreqsCount == 0:
                temp.append(vertex)
  
    
class CourseClass:
    def __init__(self, courses):
        self.verticies = []
        self.graph = {}
        for course in range(1, courses + 1):
            self.insert(course)
    
    def insert(self, course):
        node = Course(course)
        self.verticies.append(node)
        self.graph[course] = node
    
    def getNode(self, course):
        return self.graph[course]
    
    def addVertex(self, curr_course, next_course):
        currNode = self.getNode(curr_course)
        nextNode = self.getNode(next_course)
        currNode.depends.append(nextNode)
        nextNode.prepreqsCount += 1
    

class Course:
    def __init__(self, course):
        self.course = course
        self.depends = []
        self.prepreqsCount = 0

# without class
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        queue = []
        graph = {}
        in_count = {}
        
        for i in range(1, n + 1):
            graph[i] = []
            in_count[i] = 0
        
        for e1, e2 in relations:
            graph[e1].append(e2)
            in_count[e2] += 1
        
        for vertex in in_count:
            if in_count[vertex] == 0:
                queue.append(vertex)
        
        step = 0
        courses = 0
        
        while len(queue) != 0:
            step += 1
            temp = []
            for node in queue:
                courses += 1
                adjacent = graph[node]
                for a in adjacent:
                    in_count[a] -= 1
                    if in_count[a] == 0:
                        temp.append(a)
            
            queue = temp
        
        return step if courses == n else -1


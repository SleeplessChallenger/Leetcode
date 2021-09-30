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




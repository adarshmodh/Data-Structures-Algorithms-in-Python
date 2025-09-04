"""
New Students are arriving at college. Initially the students don't know each other, and each has a circle of friends limited to themselves. 
As the semester progresses, groups of friends form. As they arrive, each students gets an ID number, 1 to n. 
You will be given three arrays, each aligned by index. 
The first array will contain a 'queryType' which will be either 'Friend' or 'Total'. 
The next two arrays, 'students1' and 'students2', will each contain a Student ID. 
If the query type is 'Friends' the two students become friends. 
If the query type is 'Total', you must report the sum of the sizes of the groups of friends for the two students. 

Functional Description - 
Complete the function track_friend_groups in the editor below. The function must return an array of integers where the value at each index j denotes the answer for the jth query of type Total. 
track_friend_groups has the following parameter(s): n: the number of students, integer queryType [queryType[1],...queryTpe[q]]: an array of query type strings student1 [student1[1],...student1[q]]: an array of student integer ID's student2 [student2[1],...student2[q]]: an array of student integer ID's
"""

from collections import defaultdict

def dfs(graph, node, visited):
    visited.add(node)
    size = 1
    for nei in graph[node]:
        if nei not in visited:
            size += dfs(graph, nei, visited)
    return size

def track_friend_groups(n, queryType, students1, students2):
    graph = defaultdict(set)
    results = []

    for q, a, b in zip(queryType, students1, students2):
        if q == "Friend":
            graph[a].add(b)
            graph[b].add(a)
        elif q == "Total":
            visited = set()
            size_a = dfs(graph, a, visited)
            # reuse visited so we don't double count if a and b are connected
            size_b = dfs(graph, b, visited) if b not in visited else 0
            results.append(size_a + size_b)

    return results


# Example usage
n = 4
queryType = ["Friend", "Total", "Friend", "Total"]
students1 = [1, 1, 2, 1]
students2 = [2, 3, 3, 4]

print(getTheGroups(n, queryType, students1, students2))
# Output: [3, 4]



class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))  # 1-based IDs
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return
        # union by size
        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA
        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]

    def get_size(self, x):
        return self.size[self.find(x)]


def track_friend_groups(n, queryType, students1, students2):
    uf = UnionFind(n)
    results = []

    for q, a, b in zip(queryType, students1, students2):
        if q == "Friend":
            uf.union(a, b)
        elif q == "Total":
            total_size = uf.get_size(a) + uf.get_size(b)
            results.append(total_size)

    return results


# Example usage
n = 4
queryType = ["Friend", "Total", "Friend", "Total"]
students1 = [1, 1, 2, 1]
students2 = [2, 3, 3, 4]

print(getTheGroups(n, queryType, students1, students2))
# Output: [2, 4]

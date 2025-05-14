import math

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def cluster_2d_points(points, d):
    clusters = []
    visited = set()

    def dfs(point_idx, cluster):
        visited.add(point_idx)
        cluster.append(points[point_idx])
        for i, other_point in enumerate(points):
            if i not in visited and euclidean_distance(points[point_idx], other_point) <= d:
                dfs(i, cluster)

    for i in range(len(points)):
        if i not in visited:
            cluster = []
            dfs(i, cluster)
            clusters.append(cluster)

    return clusters

# Example usage
points = [(1, 2), (2, 3), (10, 10), (10.5, 10.1), (20, 20)]
d = 1.0
clusters = cluster_2d_points(points, d)

# Print results
for idx, cluster in enumerate(clusters):
    print(f"Cluster {idx}: {cluster}")

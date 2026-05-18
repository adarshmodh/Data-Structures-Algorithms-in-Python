import math
from collections import defaultdict
"""
each bbox of a person has XYWH values
people = [
    [10, 10, 20, 40],   # Person 0
    [25, 15, 20, 40],   # Person 1 (close to 0)
    [40, 20, 20, 40],   # Person 2 (close to 1)
    [300, 300, 20, 40]  # Person 3 isolated
]

threshold = 40

result = count_people_in_crowds(people, threshold)

print(result)
"""

def euclidean_distance(p1, p2):
    """
    Compute Euclidean distance between two 2D points.
    """
    return math.sqrt((p1[0] - p2[0])**2 +
                     (p1[1] - p2[1])**2)


def count_people_in_crowds(people_xywh, distance_threshold):
    """
    Count how many people belong to crowds.

    Parameters
    ----------
    people_xywh : List[List[float]]
        List of bounding boxes in format [x, y, w, h]

    distance_threshold : float
        Maximum center distance to consider two people connected

    Returns
    -------
    int
        Number of people that belong to crowds
    """

    n = len(people_xywh)

    # ---------------------------------------------------------
    # Step 1: Compute bbox centers
    # ---------------------------------------------------------
    centers = []

    for x, y, w, h in people_xywh:
        cx = x + w / 2.0
        cy = y + h / 2.0
        centers.append((cx, cy))

    # ---------------------------------------------------------
    # Step 2: Build graph
    #
    # If two people are close enough,
    # connect them with an undirected edge.
    # ---------------------------------------------------------
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):

            dist = euclidean_distance(centers[i], centers[j])

            if dist <= distance_threshold:
                graph[i].append(j)
                graph[j].append(i)

    # ---------------------------------------------------------
    # Step 3: Find connected components using DFS
    # ---------------------------------------------------------
    visited = set()

    def dfs(node, component):
        visited.add(node)
        component.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    # ---------------------------------------------------------
    # Step 4: Count people belonging to crowds
    #
    # Crowd = connected component with >= 2 people
    # ---------------------------------------------------------
    crowd_people_count = 0

    for person_idx in range(n):

        if person_idx not in visited:

            component = []
            dfs(person_idx, component)

            # Single isolated person is NOT a crowd
            if len(component) >= 2:
                crowd_people_count += len(component)

    return crowd_people_count

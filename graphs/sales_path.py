"""
Simple graph traversal and calculating minimum sum at every node 
Time complexity O(n)
Space complexity O(1)

"""

def get_cheapest_cost(rootNode):
  
  min_cost = float('inf')
  
  if rootNode.children == []:
    return rootNode.cost
  
  for child in rootNode.children:
    path_cost = get_cheapest_cost(child)
    if path_cost < min_cost:
      min_cost = path_cost
    
  return min_cost + rootNode.cost  

def get_cheapest_cost_it(rootNode):
	stack = [(rootNode, rootNode.cost)]
	min_path = float('inf')

	while stack:
		node, curr_cost = stack.pop()
		
		if not node.children:
			min_path = min(min_path, curr_cost)
		else:
			for child in node.children:
				stack.append((child, child.cost + curr_cost))

	return min_path

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:
  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

    
newtree = Node(0)
newchilds1,newchilds2,newchilds3 = Node(5),Node(3),Node(6)
newtree.children = [newchilds1,newchilds2,newchilds3]

print(get_cheapest_cost_it(newtree))

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.helper_insert(self.root,new_val)
        pass

    def search(self, find_val):
        return self.helper_search(self.root,find_val)
    
    
    def helper_insert(self,start,new_val):
        if new_val < start.value:
            if start.left != None:
                self.helper_insert(start.left,new_val)
            else:
                start.left = Node(new_val) 

        if new_val > start.value:
            if start.right != None:
                self.helper_insert(start.right,new_val)
            else:
                start.right = Node(new_val)

    def helper_search(self,start,find_val):
        if start!= None:
            if start.value == find_val:
                return True
            elif start.value<find_val:
                return self.helper_search(start.right,find_val)
            elif start.value>find_val:
                return self.helper_search(start.left,find_val)
                
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        answer = []
        
        answer = self.preorder_print(self.root,answer)
        
        strings = [str(integer) for integer in answer]
        return "-".join(strings)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        
        if start!=None:
            traversal.append(start.value)
            
            if start.left != None:
                traversal = self.preorder_print(start.left, traversal)
            if start.right != None:
                traversal = self.preorder_print(start.right, traversal)
                
        return traversal

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())
# Check search
# Should be True
print tree.search(2)
# Should be False
print tree.search(6)

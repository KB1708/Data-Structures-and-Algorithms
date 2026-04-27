class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

# 1) Method to add a child 
def add_child(treeNode, data):
    treeNode.children.append(data)

# 2) Method to print the parents 
def print_parents(treeNode, parent=None):
    if parent is None:
        print(f"The parent of the node {str(treeNode.data)} is ---> NULL")
    else:
        print(f"The parent of the node {str(treeNode.data)} is ---> {parent.data}")

    # Call the same function for the children of the given node 
    for child in treeNode.children:
        print_parents(child, treeNode)

# 3) Method to print the children
def print_children(treeNode):

    children_str = " ".join(str(child.data) for child in treeNode.children)
    print(f"The Children of Node {str(treeNode.data)} are {children_str}")

    # Call the func for other children nodes
    for child in treeNode.children: 
        print_children(child)

# 4) Method to print the leaf nodes
def print_leaves(treeNode):

    if treeNode.children is None:
        print(f"Leaf Node is {str(treeNode.data)}")
        return
    
    for child in treeNode.children:
        print_leaves(child)

# 5) Method to print the degree of the nodes in the tree
def print_degree(treeNode, parent=None):
    degree = len(treeNode.children)
    if parent is not None:
        degree += 1

    print(f"The degree of the node {str(treeNode.data)} is {degree}")

    for child in treeNode.children:
        print_degree(child, treeNode)
    


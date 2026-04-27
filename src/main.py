from arrays.alternate_element import AlternateElement 
from arrays.leaders import Leaders 
from tree.tree import *

if __name__ == "__main__":

    root_node = treeNode(1)

    # adding children for root node

    n2 = treeNode(2)
    n3 = treeNode(3)
    n4 = treeNode(4)

    add_child(root_node,n2)
    add_child(root_node,n3)
    add_child(root_node,n4)

    # adding children for root node n2
    n5 = treeNode(5)
    n6 = treeNode(6)

    add_child(n2,n5)
    add_child(n2,n6)

    print_parents(root_node)
    print_leaves(root_node)
    print_degree(root_node)
    print_children(n2)

    

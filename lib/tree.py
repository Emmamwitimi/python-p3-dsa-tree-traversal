class Tree:
    def __init__(self, node):
        self.root = node

    def get_element_by_id(self, node_id):
        # Depth-first traversal using recursion
        return self.depth_first_traversal(self.root, node_id)

    def depth_first_traversal(self, node, node_id):
        # Check if the current node has the matching id
        if node['id'] == node_id:
            return node
        
        # Recursively search in the children
        for child in node['children']:
            result = self.depth_first_traversal(child, node_id)
            if result:  # If we found the node, return it
                return result
        
        # Return None if no match is found
        return None

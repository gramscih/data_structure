class GHCBinaryTree:
    def __init__(self):
        self.__node = None
        self.left_node = None
        self.right_node = None

    def is_empty(self):
        return not self.__node
    
    def add(self, item):
        if not self.__node:
            self.__node = item
            self.left_node = GHCBinaryTree()
            self.right_node = GHCBinaryTree()
class TreeNode:
    def __init__(self, Value=0):
        super().__init__()
        self.Value = Value
        self.LeftSubtreeHeight = 0
        self.RightSubtreeHeight = 0
        self.Left = None
        self.Right = None
        # print("Tree Node initialized with value", self.Value)

    def get_left(self):
        return self.Left

    def get_right(self):
        return self.Right

    def set_left(self, Left):
        if type(Left) == TreeNode:
            self.Left = Left
        else:
            self.Left = TreeNode(Left)
        self.LeftSubtreeHeight += 1

    def set_right(self, Right):
        if type(Right) == TreeNode:
            self.Right = Right
        else:
            self.Right = TreeNode(Right)
        self.RightSubtreeHeight += 1

    def get_height(self):
        return max(self.LeftSubtreeHeight, self.RightSubtreeHeight)

    def __str__(self):
        return str.format('Tree Node with value {} and \nLeft Subtree \n{} \nand Right Subtree \n{}', self.Value,
                          self.Left,
                          self.Right)

class TreeNode():
    def __init__(self, Value):
        super().__init__()
        self.Value = Value
        self.Left = None
        self.Right = None
        print("Tree Node initialized with value", self.Value)

    def get_left_subtree(self):
        return self.Left

    def get_right_subtree(self):
        return self.Right

    def __str__(self):
        return str.format("Tree Node with value {} and Left Subtree {} and Right Subtree {}", self.Value, self.Left,
                          self.Right)

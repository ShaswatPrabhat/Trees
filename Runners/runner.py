from Node.node import TreeNode

if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)

    t1.set_left(t2)
    t1.set_right(t3)
    t2.set_left(t4)
    t2.set_right(t5)
    t5.set_left(t6)

    # t1.in_order_traverse()
    t1.post_order_traverse()
    # t1.pre_order_traverse()

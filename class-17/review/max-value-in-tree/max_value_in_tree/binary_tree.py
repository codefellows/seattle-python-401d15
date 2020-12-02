"""


     At every chamber we need to know 3 things that inform a 4th thing (the max value)
     What is the number on the current wall?
     What is the highest number found to the left?
     What is the highest number found to the right

     Once gathered are any higher than max_value (seen so far)


    # NOTE: there is a recursive nature here
    "Top" guide notices value on the wall
    then sends folks down to left to determine the highest value on that side
    then send folks down to right to determine the highest value on that side
    Then selects the max of the 3 values and lets the "higher up" guide now

"""
 #         12
#       27   -234



# max_value = 0 # global (but really module) level

class BinaryTree:
    def __init__(self):
        self.root = None

    def find_max(self):

        if not self.root:
            raise Exception("Tree is empty silly")

        # input: root (Node or None), max_so_far int
        # output: int
        def walk(root, max_so_far):

            if not root:
                return max_so_far

            if root.value > max_so_far:
                max_so_far = root.value # the number on current wall

            highest_left = walk(root.left, max_so_far)

            highest_right = walk(root.right, max_so_far)

            return max(max_so_far, highest_left, highest_right)

        return walk(self.root, self.root.value)









class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


if __name__ == "__main__":
    tree = BinaryTree()
    _12 = Node(12)
    _27 = Node(27)
    _neg234 = Node(-234)

    _12.left = _27
    _12.right = _neg234

    tree.root = _12


    assert tree.find_max() == 27

    print("TESTS PASSED")



class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None


  def find_maximum_value(self):

    # will need to walk through tree and find max_value
    # probably recursively

    max_value = "TODO" # an int most likely

    def walk(root):
      nonlocal max_value

      if not root:
        return

      #compare and update max_value as needed
      # e.g.
      max_value = root.value
      # print(max_value)


      walk(root.left)
      walk(root.right)

    walk(self.root)

    return max_value


  # Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.

  def pre_order(self):

    # return list of values ordered correctly
    values = []

    def walk(root):

      if not root:
        return

      # print(root.value)
      values.append(root.value)

      walk(root.left)
      walk(root.right)

    walk(self.root)

    print(values)

    return values # e.g. ["A","B","C"]

  def in_order(self):

    values = []

    def walk(root):

      if not root:
        return

      walk(root.left)
      # print(root.value)
      values.append(root.value)
      walk(root.right)

    walk(self.root)

    print(values)

    return values

  def post_order(self):

    values = []

    def walk(root):

      if not root:
        return

      walk(root.left)
      walk(root.right)
      # print(root.value)
      values.append(root.value)



    walk(self.root)

    print(values)

    return values



class BinarySearchTree(BinaryTree):


  def add(self, value):
    node = Node(value)

    if not self.root:
      self.root = node
      return


    def walk(root):
      if value < root.value:

        if not root.left:
          root.left = node
        else:
          # recurse, aka keep walking
          walk(root.left)

      else:

        if not root.right:
          root.right = node
        else:
          # recurse, aka keep walking
          walk(root.right)

    walk(self.root)

  def contains(self, target):
    """
    search the tree for a given value
    return true if found else false
    should be efficient. Aka O(h) time -- O(h) is same as O(logN) when tree is balanced

    target = 5
    result = True

        10
      5     17
        6     21
    """

    # target 4
    def walk(root): # {10} line 131 -> False | {5} line 131 -> False | None -> False

      if not root:
        return False

      if root.value == target:
        return True


      if root.value > target:
        return walk(root.left)
      else:
        return walk(root.right)


    found = walk(self.root) # False

    return found


def run_contains_tests():
  tree = create_sample_tree()
  assert tree.contains(10)
  assert tree.contains(5)
  assert tree.contains(15)
  assert not tree.contains(7)
  print("Tests Passed")

def create_sample_tree():

  tree = BinarySearchTree()

  #     10
  #   5     15

  a = Node(10)
  b = Node(5)
  c = Node(15)

  tree.root = a
  a.left = b
  a.right = c

  return tree


def do_traversals():
  tree = create_sample_tree()


  tree.add(20)


  #     10
  #   5     15
  #           20

  tree.add(0)

    #    10
  #   5     15
  # 0          20

  tree.add(20)

    #    10
  #   5     15
  # 0          20
  #          19   20
  # print("pre-order")
  # tree.pre_order()
  print("in-order")
  tree.in_order()
  # print("post-order")
  # tree.post_order()


if __name__== "__main__":
  run_contains_tests()






class Node:
  def __init__(self, value, next_=None):
    self.value = value
    self.next = next_


class LinkedList:

  def __init__(self, values=None):
    self.head = None
    if values:
      # start, stop, step for slicing
      # O(n) FTW
      for value in reversed(values):
        self.insert(value)


  def __str__(self):

    output = ""

    current = self.head

    while current:
      output += f"{{ {current.value} }} -> "
      current = current.next

    return output + "NULL"

  def insert(self, value):
    self.head = Node(value, self.head)

  def insert_after(self, value, new_value):
    if not self.head:
      return

    current = self.head

    # apples, bananas
    while current:
      if current.value == value:
        current.next = Node(new_value, current.next)
        return

      current = current.next




  def insert_before(self, value, new_value):
    if not self.head:
      return

    if self.head.value == value:
      self.insert(new_value)
      return

    current = self.head

    while current.next:

      if current.next.value == value:
        current.next = Node(new_value, current.next)
        return

      current = current.next



  def append(self, value):

    node = Node(value) # { cucumbers } -> None

    if not self.head:
      self.head = node
      return

    current = self.head

    while current.next:
      current = current.next

    current.next = node


######################
## TESTS
######################

# initialize with List
ll = LinkedList(["apples","bananas","cucumbers"])
actual = str(ll)
expected = "{ apples } -> { bananas } -> { cucumbers } -> NULL"

assert actual == expected, actual

# append
ll = LinkedList()
assert str(ll) == "NULL"
ll.append("apples")
assert str(ll) == "{ apples } -> NULL"
ll.append("bananas")
assert str(ll) == "{ apples } -> { bananas } -> NULL"


#insert before
ll = LinkedList(["apples"])

# before head
ll.insert_before("apples","bananas")
actual = str(ll)
expected = "{ bananas } -> { apples } -> NULL"
assert actual == expected, actual

# in middle
ll.insert_before("apples","cucumbers")
actual = str(ll)
expected = "{ bananas } -> { cucumbers } -> { apples } -> NULL"
assert actual == expected, actual

# TODO: insert before a value that wasn't found




#insert after
ll = LinkedList()
ll.append("apples")

# after head
ll.insert_after("apples","bananas")
actual = str(ll)
expected = "{ apples } -> { bananas } -> NULL"
assert actual == expected, actual

# in middle
ll.insert_after("apples","cucumbers")
actual = str(ll)
expected = "{ apples } -> { cucumbers } -> { bananas } -> NULL"
assert actual == expected, actual

# at end
ll.insert_after("bananas","dates")
actual = str(ll)
expected = "{ apples } -> { cucumbers } -> { bananas } -> { dates } -> NULL"
assert actual == expected, actual



print("*" * 30)
print ("**" + "ALL TESTS PASS".center(26) + "**")
print("*" * 30)

# E.g. raising an exception
# k = 60
# if k > 10 :
#   raise IndexError(f"{k} is out of range")

#   v
# { a } -> { b } -> { c } -> NULL
#
# { 1 } -> { 2 } -> { 3 } -> NULL
#   ^

# { a }  { b }    { c }
#   |    / |.    /. |
#.  v   /. v.   /.  V
# { 1 }  { 2 }    { 3 } -> NULL

# { a } -> { 1 } -> { b } -> { 2 } -> { c } -> { 3 } -> NULL


def zip(list1, list2):
  current_1 = list1.head # { a }
  current_2 = list2.head # { 1 }
  temp_1 = current_1.next  # { b }
  temp_2 = current_2.next # { 2 }

  current_1.next = current_2
  current_2.next = temp_1

  # rest is up to you

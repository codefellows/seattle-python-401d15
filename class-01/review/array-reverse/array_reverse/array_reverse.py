def reverse_array(arr):
    """
    Algorithm:
    Start
        left = 0
        right = array length - 1
    While left < right
        swap left and right values
        left increments by 1
        right decrements by 1

    return array

    L
    c,b,a
        R

    """
    leftIndex = 0
    rightIndex = len(arr) - 1

    while leftIndex < rightIndex:

        # swap left and right values
        arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]

        # alternately
        # rightVal = arr[rightIndex]
        # arr[rightIndex] = arr[leftIndex]
        # arr[leftIndex] = rightVal

        leftIndex += 1
        rightIndex -= 1

    return arr


assert reverse_array([6,2,3]) == [3,2,6,1000], 'Oops. First test No bueno'
assert reverse_array([6,2,3,4]) == [4,3,2,6], 'Oops. Second Test No bueno'

print("*" * 40)
print("WOOHOO. TESTS PASSED")
print("*" * 40)


from array_reverse import __version__
from array_reverse.array_reverse import reverse_array

def test_reverse_odd():
    lst = ["apples","bananas","cucumbers"]
    reverse_array(lst)
    assert lst == ["cucumbers","bananas","apples"]

def test_reverse_even():
    lst = ["apples","bananas","cucumbers","dates"]
    reverse_array(lst)
    assert lst == ["dates", "cucumbers","bananas","apples"]

def test_reverse_dupes():
    lst = ["apples","bananas","cucumbers","dates","apples"]
    reverse_array(lst)
    assert lst == ["apples","dates", "cucumbers","bananas","apples"]

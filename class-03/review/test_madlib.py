import pytest
from madlib_cli.madlib import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template("madlib_cli/assets/easy_peasy.txt")
    expected = "A {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "A {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "A {} and {} {}."
    expected_parts = ["Adjective", "Adjective", "Noun"]

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge():
    actual = merge("A {} and {} {}.", ["dark", "stormy", "night"])
    expected = "A dark and stormy night."
    assert actual == expected


# Not required: just shows how to test for an exception
# @pytest.mark.skip("pending")
# def test_read_template_raises_exception_with_bad_path():

#     with pytest.raises(FileNotFoundError):
#         path = "spam_and_eggs.txt"
#         read_template(path)

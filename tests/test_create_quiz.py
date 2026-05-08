

from modes import create_quiz as cq


def test_check_number():
    assert cq.check_number("4") == 4
    assert cq.check_number("  4  ") == 4
    assert cq.check_number("a") == None
    assert cq.check_number("") == None


def test_add_item():
    dct = [{"term": "apple", "definition": "red",}]
    assert cq.add_item("grapes - purple", dct) == True
    assert cq.add_item("  banana   -   yellow  ", dct) == True
    assert cq.add_item("banana-yellow", dct) == False
    assert cq.add_item("banana = yellow", dct) == False
    assert cq.add_item("banana", dct) == False
    assert cq.add_item("", dct) == False
    assert cq.add_item("apple - red", dct) == False
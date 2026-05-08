

from checker import checker as ck


def test_checker():
    dct = {"a": "apple",}
    assert ck.checker("a", dct) == "apple"
    assert ck.checker("  a  ", dct) == "apple"
    assert ck.checker("A", dct) == "apple"
    assert ck.checker("b", dct) == None
    assert ck.checker("", dct) == None


def test_if_yes():
    assert ck.if_yes("y") == True
    assert ck.if_yes("  y  ") == True
    assert ck.if_yes("Y") == True
    assert ck.if_yes("n") == False
    assert ck.if_yes("") == False


def test_check_quizzes():
    lst = ["fruits.csv",]
    empty_lst = []
    assert ck.check_quizzes(lst) == True
    assert ck.check_quizzes(empty_lst) == False


def test_check_score():
    total = 10
    assert ck.check_score(10, total) == ("A perfect score, bravo!", "=========================")
    assert ck.check_score(8, total) == ("What a great run!", "===================")
    assert ck.check_score(5, total) == ("Well done! Solid work.", "========================")
    assert ck.check_score(3, total) == ("You're getting there!", "=======================")
    assert ck.check_score(0, total) == ("A great learning opportunity!", "===============================")


def test_check_prefix():
    dct = {"r-": "rename",}
    assert ck.check_prefix("r-", dct) == ("r-", "rename")
    assert ck.check_prefix("  r-  ", dct) == ("r-", "rename")
    assert ck.check_prefix("R-", dct) == ("r-", "rename")
    assert ck.check_prefix("r", dct) == (None, None)
    assert ck.check_prefix("", dct) == (None, None)


def test_check_name():
    lst = ["fruits_and_colors.csv",]
    assert ck.check_name("colors_and_fruits", lst) == (True, "colors_and_fruits")
    assert ck.check_name("colors and fruits", lst) == (True, "colors_and_fruits")
    assert ck.check_name("fruits_and_colors", lst) == (False, "fruits_and_colors")
    assert ck.check_name("fruits and colors", lst) == (False, "fruits_and_colors")
    assert ck.check_name("", lst) == (None, None)
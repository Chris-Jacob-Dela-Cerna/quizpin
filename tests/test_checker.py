

from utils import validation as val
from utils import scoring as scr
from utils import commands as com


def test_checker():
    dct = {"a": "apple",}
    assert val.checker("a", dct) == "apple"
    assert val.checker("  a  ", dct) == "apple"
    assert val.checker("A", dct) == "apple"
    assert val.checker("b", dct) == None
    assert val.checker("", dct) == None


def test_if_yes():
    assert val.if_yes("y") == True
    assert val.if_yes("  y  ") == True
    assert val.if_yes("Y") == True
    assert val.if_yes("n") == False
    assert val.if_yes("") == False


def test_check_quizzes():
    lst = ["fruits.csv",]
    empty_lst = []
    assert val.check_quizzes(lst) == True
    assert val.check_quizzes(empty_lst) == False


def test_check_score():
    total = 10
    assert val.check_score(10, total) == ("A perfect score, bravo!", "=========================")
    assert val.check_score(8, total) == ("What a great run!", "===================")
    assert val.check_score(5, total) == ("Well done! Solid work.", "========================")
    assert val.check_score(3, total) == ("You're getting there!", "=======================")
    assert val.check_score(0, total) == ("A great learning opportunity!", "===============================")


def test_check_prefix():
    dct = {"r-": "rename",}
    assert val.check_prefix("r-", dct) == ("r-", "rename")
    assert val.check_prefix("  r-  ", dct) == ("r-", "rename")
    assert val.check_prefix("R-", dct) == ("r-", "rename")
    assert val.check_prefix("r", dct) == (None, None)
    assert val.check_prefix("", dct) == (None, None)


def test_check_name():
    lst = ["fruits_and_colors.csv",]
    assert val.check_name("colors_and_fruits", lst) == (True, "colors_and_fruits")
    assert val.check_name("colors and fruits", lst) == (True, "colors_and_fruits")
    assert val.check_name("fruits_and_colors", lst) == (False, "fruits_and_colors")
    assert val.check_name("fruits and colors", lst) == (False, "fruits_and_colors")
    assert val.check_name("", lst) == (None, None)


from utils import scoring as scr


def test_check_score():
    total = 10
    assert scr.check_score(10, total) == ("A perfect score, bravo!", "=========================")
    assert scr.check_score(8, total) == ("What a great run!", "===================")
    assert scr.check_score(5, total) == ("Well done! Solid work.", "========================")
    assert scr.check_score(3, total) == ("You're getting there!", "=======================")
    assert scr.check_score(0, total) == ("A great learning opportunity!", "===============================")
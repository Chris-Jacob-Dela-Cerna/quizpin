

from utils import commands as com


def test_check_prefix():
    dct = {"r-": "rename",}
    assert com.check_prefix("r-", dct) == ("r-", "rename")
    assert com.check_prefix("  r-  ", dct) == ("r-", "rename")
    assert com.check_prefix("R-", dct) == ("r-", "rename")
    assert com.check_prefix("r", dct) == (None, None)
    assert com.check_prefix("", dct) == (None, None)
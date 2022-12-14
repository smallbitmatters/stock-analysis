from lxml import html

from ratio_module import Ratio

with open(r"tests/ratio_page_content", 'rb') as f:
    ratio_page_content = f.read()
ratio_tree = html.fromstring(ratio_page_content)
ratio = Ratio(ratio_tree)


def test_get_present_year_dividend_ratio():
    present_year_dividend_present_year_dividend_per_share = (
        ratio.get_present_year_dividend_present_year_dividend_per_share(
            ratio_tree))
    assert present_year_dividend_present_year_dividend_per_share != 0.00
    assert isinstance(present_year_dividend_present_year_dividend_per_share,
                      float)


def test_get_present_year_dividend_ratio1():
    present_year_dividend_present_year_dividend_per_share = (
        ratio.get_present_year_dividend_present_year_dividend_per_share_minus1(
            ratio_tree))
    assert present_year_dividend_present_year_dividend_per_share != 0.00
    assert isinstance(present_year_dividend_present_year_dividend_per_share,
                      float)


def test_get_present_year_dividend_ratio2():
    present_year_dividend_present_year_dividend_per_share = (
        ratio.get_present_year_dividend_present_year_dividend_per_share_minus2(
            ratio_tree))
    assert present_year_dividend_present_year_dividend_per_share != 0.00
    assert isinstance(present_year_dividend_present_year_dividend_per_share,
                      float)


def test_get_present_year_dividend_ratio3():
    present_year_dividend_present_year_dividend_per_share = (
        ratio.get_present_year_dividend_present_year_dividend_per_share_minus3(
            ratio_tree))
    assert present_year_dividend_present_year_dividend_per_share != 0.00
    assert isinstance(present_year_dividend_present_year_dividend_per_share,
                      float)


def test_get_present_year_dividend_ratio4():
    present_year_dividend_present_year_dividend_per_share = (
        ratio.get_present_year_dividend_present_year_dividend_per_share_minus4(
            ratio_tree))
    assert present_year_dividend_present_year_dividend_per_share != 0.00
    assert isinstance(present_year_dividend_present_year_dividend_per_share,
                      float)


def test_consistent_dividend_payout():
    assert ratio.consistent_dividend_payout(ratio_tree) == True

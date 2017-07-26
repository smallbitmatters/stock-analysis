from try_module import trying as trying
from try_module import get_correct_ratio

class Ratio:

    def __init__(self, tree):
        self.tree = tree

    def get_present_year_dividend_present_year_dividend_per_share(self, tree):
        p1 = trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[2]')
        import pdb
        pdb.set_trace()
        return p1

    def get_present_year_dividend_present_year_dividend_per_share_minus1(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[3]')

    def get_present_year_dividend_present_year_dividend_per_share_minus2(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[4]')

    def get_present_year_dividend_present_year_dividend_per_share_minus3(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[5]')

    def get_present_year_dividend_present_year_dividend_per_share_minus4(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[6]')

    def consistent_dividend_payout(self, tree):
        return all([self.get_present_year_dividend_present_year_dividend_per_share(tree) > 0,
                    self.get_present_year_dividend_present_year_dividend_per_share_minus1(tree) > 0,
                    self.get_present_year_dividend_present_year_dividend_per_share_minus2(tree) > 0,
                    self.get_present_year_dividend_present_year_dividend_per_share_minus3(tree) > 0,
                    self.get_present_year_dividend_present_year_dividend_per_share_minus4(tree) > 0])

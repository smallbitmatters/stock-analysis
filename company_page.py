from try_module import trying as trying


class CompanyPage:

    def __init__(self, tree):
        self.tree = tree

    def get_pe_ratio(self, tree):
        return trying(tree, '//*[@id="div_rcard_more"]/div[1]/div[2]')

    def get_eps(self, tree):
        return trying(tree, '//*[@id="div_rcard_more"]/div[2]/div[2]')

    def get_price_of_stock(self, tree):
        return trying(tree, '//*[@id="ltpid"]')

    def get_fifty_two_wk_high(self, tree):
        return (
            float(
                tree.xpath('//*[@id="FiftyTwoHighlow"]/text()')[0]
                .split()[0]
                .replace(",", "")
            )
        )

    def get_fifty_two_wk_low(self, tree):
        return (
            float(
                tree.xpath('//*[@id="FiftyTwoHighlow"]/text()')[0]
                .split()[-1]
                .replace(",", "")
            )
        )

    def _sheet_links(self, tree, this_xpath):
        """TODO: Docstring for _sheet_links.

        :tree: TODO
        :xpath: TODO
        :returns: TODO

        """
        try:
            _sheet_links = tree.xpath(this_xpath)
            _sheet_link = _sheet_links[0].attrib['href']
            _sheet_link = _sheet_link.replace('//money', 'http://money')
        except KeyError:
            _sheet_link = ""
        return _sheet_link

    def get_balance_sheet_link(self, tree):
        return self._sheet_links(tree, '//*[@id="div_res_centre_more"]/a[4]')

    def get_ratio_link(self, tree):
        return self._sheet_links(tree, '//*[@id="div_res_centre_more"]/a[11]')

    def get_volume(self, tree):
        """TODO: Docstring for get_volume.

        :tree: TODO
        :returns: TODO

        """
        volm = tree.xpath('//*[@id="Volume"]/text()')
        return int(volm[0].replace(",", ""))

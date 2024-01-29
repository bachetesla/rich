from ._client import Wallex
from ..Base import Gather, GatherResult


class Gather_usdt_toman(Gather):
    """
    Gather USDT BID and Price
    """

    def do(self):
        """
        Gather last, bid, ask prices for usdt, toman
        :return:
        """
        usdt_toman = Wallex().markets()['USDTTMN']['stats']

        return GatherResult(ask=usdt_toman['askPrice'],
                            bid=usdt_toman['bidPrice'],
                            last=usdt_toman['lastPrice'])



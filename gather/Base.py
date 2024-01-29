"""
Gather Base
"""
from prometheus_client import CollectorRegistry

class GatherResult:
    ask: float = None
    bid: float = None
    last: float = None

    def __init__(self, ask: float, bid: float, last: float):
        self.ask = ask
        self.bid = bid
        self.last = last

    def __str__(self):
        return f"ASK: {self.ask} | BID: {self.bid} | last: {self.last}"


class Gather:
    """
    This is base class for gather it has functions needs to be gathered
    """
    prometheus_registry: CollectorRegistry = None

    def __init__(self, prometheus_registry: CollectorRegistry):
        self.prometheus_registry = prometheus_registry

    def do(self) -> GatherResult:
        """
        Implement this method.
        This method Should Return Float
        :return:
        """
        raise NotImplementedError("This called from a base class, please implement it.")

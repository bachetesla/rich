"""
This is main
"""
import time
import importlib
import threading
from prometheus_client import Gauge
from prometheus_client import start_http_server, CollectorRegistry
from util.config import RichConf
from gather.Base import GatherResult
REGISTRY = CollectorRegistry(auto_describe=True)


# from gather.wallex.usdt_toman import Gather_usdt_toman
#
# client = Gather_usdt_toman()
#
# print(client.do().last)
LABEL_NAMES = ['market', 'exchange']

ASK_PRICE = Gauge('rich_ask_price', "rich_ask_price", registry=REGISTRY, labelnames=LABEL_NAMES)
BID_PRICE = Gauge('rich_bid_price', "rich_bid_price", registry=REGISTRY, labelnames=LABEL_NAMES)
LAST_PRICE = Gauge('rich_last_price', "rich_last_price", registry=REGISTRY, labelnames=LABEL_NAMES)


def gather_up(gather_services):
    """
    Gather IT UP!
    :param gather_services:
    :return:
    """
    for service in gather_services:
        for service_name, service_data in service.items():
            service_module = service_data['module']

            # 0 Load The module
            module = importlib.import_module(f"gather.{service_module}")
            _class = getattr(module, f"Gather_{service_module.split('.')[1]}")(REGISTRY)
            result: GatherResult = _class.do()
            print(f"WORKING[{service_name}] || {result}")
            ASK_PRICE.labels(market=service_name, exchange=service_module.split('.')[0]).set(result.ask)
            BID_PRICE.labels(market=service_name, exchange=service_module.split('.')[0]).set(result.bid)
            LAST_PRICE.labels(market=service_name, exchange=service_module.split('.')[0]).set(result.last)


if __name__ == "__main__":
    config = RichConf().conf
    start_http_server(
        port=config['prometheus']['http']['port'],
        addr=config['prometheus']['http']['host'],
        registry=REGISTRY
    )

    while True:
        print("Doing Job...")
        gather_up(gather_services=config['gather'])
        time.sleep(config['general']['interval_seconds'])

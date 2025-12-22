import copy
# 日志模块
import logging
import json
import ssl
import sys
import time
# 依赖 websocket-client 库，需先用 pip 安装
import websocket

log = logging.getLogger(__name__)

class OrderBoook(object):
    BIDS = "bid"
    ASKS = "ask"

    def __init__(self, limit=20):
        self.limit = limit
        self.bids = {}
        self.asks = {}
        self.bids_sorted = []
        self.asks_sorted = []
    
    def insert(self, price, amount, direction):
        if direction == self.BIDS:
            if amount == 0:
                if price in self.bids:
                    del self.bids[price]
            else:
                self.bids[price] = amount
                print("BID: {} / {}".format(price, amount))
        elif direction == self.ASKS:
            if amount == 0:
                if price in self.asks:
                    del self.asks[price]
            else:
                self.asks[price] = amount
                print("ASK: {} / {}".format(price, amount))
        else:
            print("WARNING: unknown direction {}".format(direction))
    
    def sort_and_truncate(self):
        self.bids_sorted = sorted([(price, amount) for price, amount in self.bids.items()], reverse=True)
        self.asks_sorted = sorted([(price, amount) for price, amount in self.asks.items()])
        self.bids_sorted = self.bids_sorted[:self.limit]
        self.asks_sorted = self.asks_sorted[:self.limit]
        self.bids = dict(self.bids_sorted)
        self.asks = dict(self.asks_sorted)
    
    def get_copy_of_bids_and_asks(self):
        return copy.deepcopy(self.bids_sorted), copy.deepcopy(self.asks_sorted)

class Crawler:
    def __init__(self, symbol, output_file):
        self.orderbook = OrderBoook(limit=10)
        self.output_file = output_file
        self.ws = websocket.WebSocketApp(
            "wss://api.gemini.com/v1/marketdata/{}".format(symbol),
            on_message=lambda ws, message: self.on_message(message),
            on_error=self.on_error,
        )
        # 设置代理
        self.ws.run_forever(
            sslopt={"cert_reqs": ssl.CERT_NONE},
            # 设置 HTTP 代理的话，websocket 会无法连接
            # http_proxy_host="127.0.0.1",
            # http_proxy_port=1080,
            # http_proxy_auth=None
        )
    
    def on_message(self, message):
        data = json.loads(message)

        for event in data["events"]:
            price, amount, direction = float(event["price"]), float(event["remaining"]), event["side"]
            self.orderbook.insert(price, amount, direction)
        
        self.orderbook.sort_and_truncate()

        with open(self.output_file, "a+") as f:
            bids, asks = self.orderbook.get_copy_of_bids_and_asks()
            output = {
                "bids": bids,
                "asks": asks,
                "ts": int(time.time() * 1000)
            }
            f.write(json.dumps(output) + "\n")
    
    def on_error(self, error):
        print(error, file=sys.stderr)

if __name__ == "__main__":
    symbol = "BTCUSD"
    logging.basicConfig(
        filename="{}".format(symbol)
    )
    crawler = Crawler(symbol="BTCUSD", output_file="BTCUSD.log")

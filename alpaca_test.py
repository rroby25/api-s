from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.live import StockDataStream
trading_client = TradingClient("PKN9ELM468JKILE96YEB","hlL9ecKegcdCCOPaQgVc3UhSZI3MUiqzSAEM0xHx")

stream = StockDataStream("PKN9ELM468JKILE96YEB","hlL9ecKegcdCCOPaQgVc3UhSZI3MUiqzSAEM0xHx")

async def handle_trade(data):
    print(data)

stream.subscribe_trades(handle_trade, "AAPL")

stream.run()
# positions = trading_client.get_all_positions()

# print(trading_client.get_all_positions())

# for pos in positions:
#     print(pos.symbol, pos.current_price)


# market_order_data= MarketOrderRequest(
#     symbol="SPY",
#     qty=100,
#     side=OrderSide.BUY,
#     time_in_force=TimeInForce.DAY,
# )
# market_order_data= LimitOrderRequest(
#     symbol="AAPL",
#     qty=1,
#     side=OrderSide.BUY,
#     time_in_force=TimeInForce.DAY,
#     limit_price = 200.00,
# )

# request_params = GetOrdersRequest(
#     status=QueryOrderStatus.OPEN,
# )

# orders = trading_client.get_orders(request_params)

# for order in orders:
#     trading_client.cancel_order_by_id(order.id)

# market_order = trading_client.submit_order(market_order_data)

# print(market_order)

























# print(trading_client.get_account().account_number)
# print(trading_client.get_account().buying_power)

# from alpaca.data import StockHistoricalDataClient, StockTradesRequest
# from datetime import datetime

# data_client = StockHistoricalDataClient("PKN9ELM468JKILE96YEB","hlL9ecKegcdCCOPaQgVc3UhSZI3MUiqzSAEM0xHx")

# request_params = StockTradesRequest(
#     symbol_or_symbols="AAPL",
#     start=datetime(2024, 1, 30, 14, 30), 
#     end=datetime(2024, 1, 30, 14, 45)
# )

# trades = data_client.get_stock_trades(request_params)

# for trade in trades.data["AAPL"]:
#     print(trade)
#     break


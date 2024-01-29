from tradingview_ta import TA_Handler, Exchange, Interval

testa = TA_Handler(
    symbol='TSLA'
    screener='america',
    exchange='NASDAQ',
    interval =interval.INTERVAL_1_MINUTE
)
 
class Indicator():
    def __init__(self,data):
        self.data = data 
    def get_kline_info(self,index):
        open_price =  self.data[index][1]
        high_price =  self.data[index][2]
        low_price =   self.data[index][3]
        close_price = self.data[index][4]
        volume =      self.data[index][5]

        return open_price ,high_price ,low_price ,close_price ,volume 

    def rsi(self,window = 14):
        data = self.data[-window:]
        positive  = []
        negative = []
        close_prices = [float(self.get_kline_info(index)[3]) for index in range(-window,0)]
        open_prices = [float(self.get_kline_info(index)[0]) for index in range(-window,0)]

        positive = [close  for close,open_ in zip(open_prices,close_prices) if close > open_]
        negative = [close  for close,open_ in zip(open_prices,close_prices) if open_ > close]
        if len(negative) == 0:
            rsi = 100
        else:
            rs = sum(positive) / sum(negative) if sum(negative) != 0 else 0
            rs = sum(positive)/ sum(negative)
            rsi = 100 - ( 100 / 1+ rs )
        order = None
        if rsi <= 30:
            order = "buy"
        elif rsi >= 70:
            order = "sell"
        return rsi , order

    def Sma(self,windows):
        pass
        ###to be continued
# region imports
from AlgorithmImports import *
# endregion

class DancingRedSeahorse(QCAlgorithm):

    def initialize(self):
        # Set start and end date for back testing
        self.set_start_date(2022, 3, 3)
        self.set_end_date(2023, 3, 3)
        # Set cash 
        self.set_cash(100000)

        # Set security that we want to trade
        spy = self.add_equity("SPY", Resolution.DAILY)
        # to add other securities from other asset classes...
        # self.add_forex, self.add_futures...

        # Set the data normalization mode for the SPY equity data
        spy.set_data_normalization_mode(DataNormalizationMode.RAW)

        # save the symbol object into a new variable
        self.spy = spy.symbol

        # set a benchmark for the algo
        self.set_benchmark("SPY")
        # set a brokerage model
        self.set_brokerage_model(BrokerageName.INTERACTIVE_BROKERS_BROKERAGE, AccountType.MARGIN)

        # Helper variables needed
        self.entry_price = 0
        self.period = timedelta(31)
        self.next_entry_time = self.time

    """
    Explanation for on_data() method: called when algo. receives data. specifically everytime a tick
    event occurs or a bar reaches its endtime.
    """
    def on_data(self, data: Slice):
        if not self.spy in data:
            return 
        # save the most recent price of the "SPY"
        price = self.securities[self.spy].close

        # check if our bot has invested
        if not self.portfolio.invested:
            # if we aren't invested, check if it's time to invest
            if self.next_entry_time <= self.time:
                self.set_holdings(self.spy, 1)
                # self.market_order(self.spy, int(self.portfolio.cash / price))
                # Log that we just bought a security at the current price (in our case "SPY")
                self.log("BUY SPY @" + str(price))
                # save the current price of "SPY" to the entry price variable
                self.entry_price = price
        elif self.entry_price * 1.1 < price or self.entry_price * 0.9 > price:
            self.liquidate(self.spy)
            # Log that spy position is closed
            self.log("SELL SPY @" + str(price))
            # set the next entry time to the next 31 days
            self.next_entry_time = self.time + self.period 

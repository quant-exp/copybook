########################################### simple version ###############################
import pandas as pd
import locale
import matplotlib.pyplot as plt
from zipline.algorithm import TradingAlgorithm
import zipline.finance.trading as trading
# from zipline.utils.factory import load_from_yahoo
from datetime import datetime, date
from pytz import timezone
import pytz
from dateutil.tz import tzutc
from dateutil.parser import parse
from zipline.finance.slippage import FixedSlippage
from zipline.finance.commission import PerShare, PerTrade

from pandas_datareader.google.daily import GoogleDailyReader

@property
def url(self):
    print("call @property get url, %s, %s"%(self, type(self)))
    return 'http://finance.google.com/finance/historical'

GoogleDailyReader.url = url



# Define algorithm
def initialize(context):
    pass

def handle_data(context, data):
    print("handle_data : %s"%data.current_dt)

# Create algorithm object passing in initialize, handle_data functions
algo_obj = TradingAlgorithm(initialize=initialize, handle_data=handle_data)

perf_manual = algo_obj.run(bars)


########################################### long version ###############################



import pandas as pd
import locale
import matplotlib.pyplot as plt
from zipline.algorithm import TradingAlgorithm
import zipline.finance.trading as trading
# from zipline.utils.factory import load_from_yahoo
from datetime import datetime, date
from pytz import timezone
import pytz
from dateutil.tz import tzutc
from dateutil.parser import parse
from zipline.finance.slippage import FixedSlippage
from zipline.finance.commission import PerShare, PerTrade

from pandas_datareader.google.daily import GoogleDailyReader

@property
def url(self):
    print("call @property get url, %s, %s"%(self, type(self)))
    return 'http://finance.google.com/finance/historical'

GoogleDailyReader.url = url

central = timezone('US/Central')
HOLDTIME = 5
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8')
COMMISSION=0.005

def date_utc(s):
    return parse(s, tzinfos=tzutc)


class BollingerBands(TradingAlgorithm):   

    def initialize(self):
        self.count = 0;
        pass

    def handle_data(self, data):
        self.count = self.count + 1
        if self.count == 2 : 
            print("handle_data, count %d : %s"%(self.count, data.current_dt))
            print(data)


if __name__ == '__main__':
    df = bars

    # # # # init Strat Class
    Strategy = BollingerBands()
    # #print df

    # # # # # # Run Strategy
    results = Strategy.run(df)
    results['algorithm_returns'] = (1 + results.returns).cumprod()


    # results.to_csv('output.csv')
    print(results['algorithm_returns'].tail(1)[0]*100)
    
    

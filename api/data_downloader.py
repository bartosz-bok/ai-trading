import yfinance as yf


class DataDownloader:
    def __init__(self):
        pass

    def download_data(self, financial_instrument_name, financial_instrument_type, data_start, data_end, frequency):
        raise NotImplementedError


class YahooDataDownloader(DataDownloader):
    def __init__(self):
        super().__init__()
        self.df_downloaded_data = None

    def download_data(self,
                      financial_instrument_name: str,
                      financial_instrument_type: str,
                      data_start: str,
                      data_end: str,
                      frequency='daily'):

        if financial_instrument_type == 'stock' and frequency == 'daily':
            self.df_downloaded_data = yf.download(tickers=financial_instrument_name,
                                                  start=data_start,
                                                  end=data_end,
                                                  progress=False,
                                                  )

    def print_downloaded_data(self, n_rows: int):
        print(self.df_downloaded_data.head(n_rows))

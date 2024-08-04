from api.data_downloader import YahooDataDownloader

if __name__ == '__main__':
    yahoo_data_downloader = YahooDataDownloader()
    name = 'AAPL'
    instrument_type='stock'
    start = '2019-01-01'
    end = '2021-06-12'
    yahoo_data_downloader.download_data(financial_instrument_name=name,
                                        financial_instrument_type=instrument_type,
                                        data_start=start,
                                        data_end=end
                                        )

    yahoo_data_downloader.print_downloaded_data(n_rows=-1)

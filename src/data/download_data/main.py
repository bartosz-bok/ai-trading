from src.data.download_data.config import DOWNLOAD_DATA_CONFIG
from src.data.download_data.data_downloader_manager import DataDownloaderManager
from src.data.download_data.data_sources.yahoo.yahoo_data_downloader import YahooDataDownloader

if __name__ == '__main__':

    data_downloaders = [
        YahooDataDownloader(),
    ]

    data_downloader_manager = DataDownloaderManager(data_downloaders)
    data_downloader_manager.execute_all(config=DOWNLOAD_DATA_CONFIG)

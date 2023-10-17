import os
import urllib.request as requests
import zipfile
from pathlib import Path
from Demand_Forecast import logger
from Demand_Forecast.utils.common import get_size
from Demand_Forecast.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig)->None:
        self.config = config

    
    def download_file(self) ->None:
        if not os.path.exists(self.config.local_data_file):
            filename, headers = requests.urlretrieve(
                url= self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f'{filename} downloaded with the following info: {headers}')
        
        else:
            logger.info(f'File already exists of size: {get_size(Path(self.config.local_data_file))}')
    
    def extract_file(self)->None:
         """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
         unzip_path = self.config.unzip_dir
         os.makedirs(unzip_path, exist_ok=True)
         with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
             zip_ref.extractall(unzip_path)
from Demand_Forecast.constants import *
from Demand_Forecast.utils.common import read_yaml, create_directories
from Demand_Forecast.entity.config_entity import DataIngestionConfig



class ConfigurationManager:
    def __init__(self, 
                 config_filepath = CONFIG_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH,
                 params_fileapth = PARAMS_FILE_PATH) ->None:
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        self.params = read_yaml(params_fileapth)

    
    def get_ingestion_data_config(self) ->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
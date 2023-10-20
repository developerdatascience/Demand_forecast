from Demand_Forecast.constants import *
from Demand_Forecast.utils.common import read_yaml, create_directories
from Demand_Forecast.entity.config_entity import (DataIngestionConfig,
                                                  DataValidationConfig,
                                                  DataTransformationConfig,
                                                  ModelTrainerConfig)



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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        return DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            unzip_data_dir= config.unzip_data_dir,
            all_schema= schema
        )
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir= config.root_dir,
            data_path = config.data_path
        )
    
    def get_model_trainer(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        schema = self.schema.TARGET_COLUMN
        params = self.params.Inventory
        fcst_parms = self.params.Forecast

        create_directories([config.root_dir])
        return ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            order= fcst_parms.order,
            seasonal_order= fcst_parms.seasonal_order,
            days_in_future = fcst_parms.days_in_future,
            initial_inventory= params.initial_inventory,
            lead_time= params.lead_time,
            service_level= params.service_level,
            holding_cost= params.holding_cost,
            stockout_cost= params.stockout_cost,
            target_column= schema.name
        )
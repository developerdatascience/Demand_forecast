from Demand_Forecast.config.configuration import ConfigurationManager
from Demand_Forecast.components.data_validation import DataValidation
from Demand_Forecast import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self) ->None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config= data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            logger.info(e)
            raise e
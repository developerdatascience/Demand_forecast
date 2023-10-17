from Demand_Forecast.components.data_transformation import DataTransformation
from Demand_Forecast.config.configuration import ConfigurationManager
from Demand_Forecast import logger


STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self) -> None:
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
        except Exception as e:
            logger.exception(e)
            raise(e)
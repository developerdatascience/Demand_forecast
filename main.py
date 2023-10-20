from Demand_Forecast import logger
from Demand_Forecast.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from Demand_Forecast.pipeline.stage_02_data_validation import DataValidationPipeline
from Demand_Forecast.pipeline.stage_03_data_transformation import DataTransformationPipeline
from Demand_Forecast.pipeline.stage_04_model_trainer import ModelTrainerPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(">>>>>>>>>>>>>Data Ingestion begins<<<<<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(">>>>>>>>>>>>>Data Ingestion completed<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(">>>>>>>>>>>>>Data Validation begins<<<<<<<<<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(">>>>>>>>>>>>>Data Validation completed<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(">>>>>>>>>>>>>Data Transformation begins<<<<<<<<<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(">>>>>>>>>>>>>Data Transformation completed<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(">>>>>>>>>>>>>Data Transformation begins<<<<<<<<<<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(">>>>>>>>>>>>>Data Transformation completed<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

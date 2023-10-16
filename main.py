from Demand_Forecast import logger
from Demand_Forecast.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(">>>>>>>>>>>>>Data Ingestion begins<<<<<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(">>>>>>>>>>>>>Data Ingestion completed<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
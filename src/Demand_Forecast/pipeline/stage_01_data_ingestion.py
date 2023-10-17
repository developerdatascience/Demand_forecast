from Demand_Forecast.config.configuration import ConfigurationManager
from Demand_Forecast.components.data_ingestion import DataIngestion
from Demand_Forecast import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self) ->None:
        pass


    def main(self)->None:
        config = ConfigurationManager()
        data_ingestion_config = config.get_ingestion_data_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_file()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} completed<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e




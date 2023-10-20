from Demand_Forecast.components.model_trainer import ModelTrainer
from Demand_Forecast.config.configuration import ConfigurationManager
from Demand_Forecast import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self) -> None:
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer()
            model_trainer = ModelTrainer(config=model_trainer_config)
            predictions = model_trainer.predictions()
            inventory_info = model_trainer.inventory_manage()
            print(inventory_info)
        except Exception as e:
            logger.exception(e)
            raise(e)
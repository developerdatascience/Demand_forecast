from Demand_Forecast.components.data_evaluation import ModelEvaluation
from Demand_Forecast.config.configuration import ConfigurationManager
from Demand_Forecast import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            logger.exception(e)
            raise e
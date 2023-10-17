import pandas as pd

from Demand_Forecast import logger
from Demand_Forecast.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                validation_status = col in all_schema
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f'Validation Status: {validation_status}')
            return validation_status
        except Exception as e:
            logger.info(e)
            raise(e)
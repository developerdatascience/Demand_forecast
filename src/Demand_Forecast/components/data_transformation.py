from Demand_Forecast.entity.config_entity import DataTransformationConfig
from Demand_Forecast import logger
import pandas as pd
from sklearn.model_selection import train_test_split
import os


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def convert_dtypes(self,data: pd.DataFrame, column_name: str, new_dtypes: str) ->pd.DataFrame:
        """
        Convert the data type of a specific column in the DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame containing the data.
            column_name (str): The name of the column to be converted.
            new_data_type (str): The desired data type for the column.
                Supported types: 'str', 'int', 'float', 'datetime'.

        Returns:
            pd.DataFrame: The DataFrame with the converted column.
        """
        if new_dtypes == "str":
            data[column_name] = data[column_name].astype(str)
            logger.info(f"Data type conversion of {column_name} to {new_dtypes} completed Successfully")
        elif new_dtypes == "int64":
            data[column_name] = data[column_name].astype("int64")
            logger.info(f"Data type conversion of {column_name} to {new_dtypes} completed Successfully")
        elif new_dtypes == "float64":
            data[column_name] = data[column_name].astype("float64")
            logger.info(f"Data type conversion of {column_name} to {new_dtypes} completed Successfully")
        elif new_dtypes == "datetime":
            data[column_name] = pd.to_datetime(data[column_name], errors='coerce')
            logger.info(f"Data type conversion of {column_name} to {new_dtypes} completed Successfully")
        else:
            logger.info(f"Data type conversion of {column_name} to {new_dtypes} could not be completed")
            raise ValueError("Unsupported data type conversion")
        
        return data
    
    def train_test_split(self) -> None:
        data = pd.read_csv(self.config.data_path)
        data = self.convert_dtypes(data=data, column_name='Date', new_dtypes='datetime')

        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test data")
        logger.info(train.shape)
        logger.info(test.shape)

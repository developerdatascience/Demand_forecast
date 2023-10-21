import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path

from Demand_Forecast.entity.config_entity import ModelEvaluationConfig
from Demand_Forecast.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config
    
    @staticmethod
    def eval_metrics(actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    @staticmethod
    def load_data(df):
        df = df[['Date', 'Product_ID', 'Demand', 'Inventory']]
        df = df.set_index('Date')
        df = df['Demand']
        return df
    
    def log_into_mlflow(self):
        test = self.load_data(df=pd.read_csv(self.config.test_data_path))
        train = self.load_data(df=pd.read_csv(self.config.train_data_path))
        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            model_fit = model.fit(disp=False)
            predictions = model_fit.predict(start=len(train), end=len(train) + len(test) -1)
            predictions = predictions.astype(int)

            (rmse, mae, r2) = self.eval_metrics(actual=test, pred=predictions)

            #saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path = Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="Time Series-SARIMAX")
            else:
                mlflow.sklearn.log_model(model, "model")




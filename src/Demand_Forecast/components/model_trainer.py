from Demand_Forecast.entity.config_entity import ModelTrainerConfig
import pandas as pd
import numpy as np
import os
from typing import Dict
import joblib
from statsmodels.tsa.statespace.sarimax import SARIMAX


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    
    @staticmethod
    def parse_tuple(input):
        return tuple(int(x) for x in input.strip('()').split(','))
    
    def predictions(self):
        train = pd.read_csv(self.config.train_data_path)
        test =  pd.read_csv(self.config.test_data_path)

        train['Date'] = pd.to_datetime(train['Date'])
        time_series = train.set_index('Date')['Demand']
        order = self.parse_tuple(input=self.config.order)
        seasonal_order = self.parse_tuple(input=self.config.seasonal_order)
        model = SARIMAX(time_series, order= order, seasonal_order= seasonal_order)
        model_fit = model.fit(disp=False)
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))

        future_steps = self.config.days_in_future
        predictions = model_fit.predict(len(time_series), len(time_series) + future_steps -1)
        predictions = predictions.astype(int)
        return predictions
    
    def inventory_manage(self) -> Dict[str, int]:
        df = pd.read_csv(self.config.train_data_path)
        df['Date'] = pd.to_datetime(df['Date'])
        time_series = df.set_index('Date')['Demand']
        predictions = self.predictions().to_list()
        
        future_dates = pd.date_range(start=time_series.index[-1] + pd.DateOffset(days=1), periods=self.config.days_in_future, freq='D')
        forecasted_demand = pd.Series(predictions, index=future_dates)
        # Initial Inventory level
        initial_inventory = self.config.initial_inventory
        # Lead time (No of days to replenish inventory)
        lead_time = self.config.lead_time # it's different for every business, 1 is an example
        # Service level (probability of not stocking out)
        service_level = self.config.service_level # it's different for every business, 0.95 is an
        # Calculate the optimal order quantity using the Newsvendor formula
        z = np.abs(np.percentile(forecasted_demand, 100 * (1 - service_level)))
        order_quantity = np.ceil(forecasted_demand.mean() + z).astype(int)
        # Calculate the reorder point
        reorder_point = forecasted_demand.mean() * lead_time + z
        # Calculate the optimal safety stock
        safety_stock = reorder_point - forecasted_demand.mean() * lead_time
        # Calculate the total cost (holding cost + stockout cost)
        holding_cost = self.config.holding_cost  # it's different for every business, 0.1 is an example
        stockout_cost = self.config.stockout_cost  # # it's different for every business, 10 is an example
        total_holding_cost = holding_cost * (initial_inventory + 0.5 * order_quantity)
        total_stockout_cost = stockout_cost * np.maximum(0, forecasted_demand.mean() * lead_time - initial_inventory)

        # Calculate the total cost
        total_cost = total_holding_cost + total_stockout_cost
        return {
            "Optimal Order Quantity" : order_quantity,
            "Reorder Point": reorder_point,
            "Safety Stock": safety_stock,
            "Total Cost": total_cost
        }
        
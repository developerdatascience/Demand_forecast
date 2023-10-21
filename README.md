# Demand_forecast
Demand Forecasting means estimating future customer demand for a product or service based on historical data and relevant factors. Inventory Optimization is the strategic management of inventory levels to ensure that the right amount of goods is available at the right time to meet customer demand while minimizing costs



Now let’s understand this output one by one:

**Optimal Order Quantity: 236** – The optimal order quantity refers to the quantity of a product that should be ordered from suppliers when the inventory level reaches a certain point. In this case, an optimal order quantity of 236 units has been calculated.

**Reorder Point: 235.25** – The reorder point is the inventory level at which a new order should be placed to replenish stock before it runs out. In this case, a reorder point of 235.25 units has been calculated, which means that when the inventory reaches or falls below this level, an order should be placed to replenish stock.

**Safety Stock: 114.45** – Safety stock is the additional inventory kept on hand to account for uncertainties in demand and supply. It acts as a buffer against unexpected variations in demand or lead time. In this case, a safety stock of 114.45 units has been calculated, which helps ensure that there’s enough inventory to cover potential fluctuations in demand or lead time.

**Total Cost: 561.80** – The total cost represents the combined costs associated with inventory management. In this case, the total cost has been calculated as approximately 561.80 units based on the order quantity, reorder point, safety stock, and associated costs.

By analyzing these values, you can make informed decisions about how much inventory to order and when to place orders to ensure a smooth supply chain and customer satisfaction while minimizing costs.



<!-- Connecting to Dagshub -->

MLFLOW_TRACKING_URI=https://dagshub.com/developerdatascience/Demand_forecast.mlflow \
MLFLOW_TRACKING_USERNAME=developerdatascience \
MLFLOW_TRACKING_PASSWORD=3f1565218d6ec2d42985b700ffecee09de158b93 \
python script.py


```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/developerdatascience/Demand_forecast.mlflow
export MLFLOW_TRACKING_USERNAME=developerdatascience
export MLFLOW_TRACKING_PASSWORD=3f1565218d6ec2d42985b700ffecee09de158b93

```
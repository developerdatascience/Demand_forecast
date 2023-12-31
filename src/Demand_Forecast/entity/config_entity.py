from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    order: Tuple[int, int, int]
    seasonal_order: Tuple[int, int, int, int]
    days_in_future: int
    initial_inventory: int
    lead_time: int
    service_level: float
    holding_cost: float
    stockout_cost: int
    target_column: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    train_data_path: Path
    model_path: Path
    fcst_params: dict
    all_inventory_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str
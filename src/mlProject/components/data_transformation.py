import os
from src.mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        train_set, test_set = train_test_split(data)

        train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Splitted data into train and test sets and saved them in {self.config.root_dir}")
        logger.info(f"Train set shape: {train_set.shape}, Test set shape: {test_set.shape}")

        print(train_set.shape)
        print(test_set.shape)


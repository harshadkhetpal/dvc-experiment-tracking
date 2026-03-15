# Author: Harshad Khetpal <harshadkhetpal@gmail.com>
# DVC + MLflow Training Stage

import mlflow, mlflow.sklearn, yaml, json, pickle, logging
import numpy as np, pandas as pd
from pathlib import Path
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import cross_val_score

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    params = {"subsample": 0.8, "max_depth": 5}
    model = GradientBoostingClassifier(**params)
    logger.info("Training complete")

if __name__ == "__main__":
    main()

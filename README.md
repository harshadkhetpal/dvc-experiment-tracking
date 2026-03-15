# 📊 DVC + MLflow — Experiment Tracking & Data Versioning

[![DVC](https://img.shields.io/badge/DVC-3.x-945DD6?style=flat-square&logo=dvc&logoColor=white)](https://dvc.org)
[![MLflow](https://img.shields.io/badge/MLflow-2.12-0194E2?style=flat-square&logo=mlflow&logoColor=white)](https://mlflow.org)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Hydra](https://img.shields.io/badge/Hydra-Config-E05735?style=flat-square)](https://hydra.cc)

> Reproducible ML experiments with DVC pipelines, MLflow tracking, Hydra config management, and automated hyperparameter tuning with Optuna. S3-backed remote storage.

## 🏗 Pipeline
```
Raw Data (S3/DVC) → Preprocess → Feature Engineering → Train → Evaluate → Register
```

## 🚀 Quick Start
```bash
git clone https://github.com/harshadkhetpal/dvc-experiment-tracking
cd dvc-experiment-tracking
pip install -r requirements.txt
dvc pull
dvc repro
```

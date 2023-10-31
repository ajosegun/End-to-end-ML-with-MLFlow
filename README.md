# End-to-end-ML-with-MLFlow

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

# How to run?

### STEPS:

Clone the repository

```bash
https://dagshub.com/ajosegun/End-to-end-ML-with-MLFlow
```

### STEP 01- Create a conda environment after opening the repository

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up you local host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd

- mlflow ui

### dagshub

[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ajosegun/End-to-end-ML-with-MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=ajosegun \
MLFLOW_TRACKING_PASSWORD=97b8498dbe402c30f6c6b1bd4a520f5415e4a110 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URL=https://dagshub.com/ajosegun/End_To_End_Project_With_MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=ajosegun

export MLFLOW_TRACKING_PASSWORD=34255e2baf836bf6327d7bb761b9ef93d83d0201

```

## About MLflow

MLflow

- Its Production Grade
- Trace all of your expriements
- Logging & tagging your model

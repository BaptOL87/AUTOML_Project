# %% import librairies 
import pandas as pd
from supervised.automl import AutoML
import IPython
import markdown
from loguru import logger 

# %% load datasets and split train test 

data_train = pd.read_csv("train_dataset.csv", encoding='UTF-8', sep=",")
data_test = pd.read_csv("test_dataset.csv", encoding='UTF-8', sep=",")

X_train = data_train.drop(columns=['TAUX_DE_REMPLISSAGE', 'TAUX_DE_VENTE', 'UPDATE_TIMESTAMP_UTC'])
y_train = data_train['TAUX_DE_REMPLISSAGE']

X_test = data_test.drop(columns=['TAUX_DE_REMPLISSAGE', 'TAUX_DE_VENTE', 'UPDATE_TIMESTAMP_UTC'])
y_test = data_test['TAUX_DE_REMPLISSAGE']

logger.info("X_train shape:")
logger.info(X_train.shape)
logger.info("y_train shape:")
logger.info(y_train.shape)
logger.info("X_test shape:")
logger.info(X_test.shape)
logger.info("y_test shape:")
logger.info(y_test.shape)

# %% fit model, predict and then generate html report 
automl = AutoML(total_time_limit=5*60, mode='Explain', random_state=42, ml_task='regression')
automl.fit(X_train, y_train)
predictions = automl.predict(X_test)
report = automl.report()  # also writes AutoML_1/README.html on disk

# %% save the html report (must stay in the results folder: the images are relative links)
with open("AutoML_1/rapport.html", "w", encoding='UTF-8') as f:
    f.write(report.data)
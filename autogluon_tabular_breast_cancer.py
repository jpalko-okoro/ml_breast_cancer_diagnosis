# -*- coding: utf-8 -*-
import pandas as pd
train_data = pd.read_csv('risk_dataset.csv')

from autogluon.tabular import TabularDataset
train_data = TabularDataset('risk_dataset.csv')

## Reformat dataset

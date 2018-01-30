import math, json, sys, os
import pandas as pd
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from utils.utils import *
from utils.kaggle import *
from utils.Training import *

t = training()
t.train_columns = [
    'TotalSF', 'OverallQual', 'YearBuilt', 'OverallCond', 'LotArea',
    'BsmtFullBath', 'TotalBsmtSF', 'MoSold'
]

t.dummify_at_init = True
t.dummify_drop_first = False
t.use_label_encoding = False

t.prepare()

t.sanity()

accuracy = test_accuracy_kfolds(t.df_train, t.labels)
print 'Coefficient of determination:', accuracy

generate_predictions(t.labels, t.df_train, t.df_test, t.test_ids)
print "Predictions complete."
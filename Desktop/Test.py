# import all of library  

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re 
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
from sklearn import tree
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV


df_trainn = pd.read_csv(r'C:\Users\Asus\Desktop\Test.csv')
sns.distplot(df_trainn['Number'])
df_trainn.describe()
values = df_trainn.skew(axis = 0, skipna = True)
print(values)

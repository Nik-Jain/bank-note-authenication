import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from CONSTANTS import *

df = pd.read_csv(INPUT)

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

classfier = RandomForestClassifier()
classfier.fit(x_train, y_train)

y_pred = classfier.predict(x_test)
score = accuracy_score(y_test, y_pred)


with open(MODEL_PATH, 'wb') as fp:
    pickle.dump(classfier, fp)

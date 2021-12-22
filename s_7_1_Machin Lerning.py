import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

df['Sex'] = df['Sex'].map({'female':0 , 'male':1})

age_mean = df['Age'].mean()

df['Age'].fillna(age_mean, inplace=True)

df[df['Sex'] == 0] ['Survived'].value_counts()

df[df['Sex'] == 1] ['Survived'].value_counts()

X = df[['Pclass' , 'Sex' , 'Age']]
y = df['Survived']

from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=1 , random_state=42)

tree.fit(X_train , y_train)

tree.score(X_test , y_test)

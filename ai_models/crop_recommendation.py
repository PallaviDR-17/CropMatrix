from sklearn.tree import DecisionTreeClassifier
import numpy as np


X = [[25, 60, 40], [30, 50, 20], [20, 70, 60]]
y = ["Maize", "Wheat", "Rice"]


model = DecisionTreeClassifier()
model.fit(X, y)


def recommend(temp, humidity, soil):
return model.predict([[temp, humidity, soil]])[0]
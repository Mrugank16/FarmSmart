# train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("Crop_recommendation.csv")

# Split data into features and target
X = data.drop('label', axis=1)
y = data['label']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Save the model
joblib.dump(model, 'trained_model/crop_recommendation_model.pkl')

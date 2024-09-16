# Importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Read file .csv cleaned
df = pd.read_csv('./AutomaticAnalysis/NewDF_cleaned_AllCategories.csv')
print(df)

# Splitting data into training and testing ones.
X = df['COMMIT:']
y = df['CATEGORIES:']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

print(y_train)

text_clf = Pipeline([
('vect', CountVectorizer()),
('tfidf', TfidfTransformer()),
('clf', SGDClassifier()),
])

text_clf.fit(X_train, y_train)

text_clf.predict(X_train)

# Training the model.
y_predicted_train = text_clf.predict(X_train)
y_predicted_test = text_clf.predict(X_test)
training_acc = round(accuracy_score(y_train, y_predicted_train), 3)
testing_acc = round(accuracy_score(y_test, y_predicted_test), 3)

# Checking accuracy.
print(f'Training Accuracy: {training_acc}')
print(f'Testing Accuracy: {testing_acc}')

df_All = pd.read_csv('./AutomaticAnalysis/Dataframe1.csv')
print(df_All)

X_All = df_All['CommitName']
print(text_clf.predict(X_All))

df_All.insert(2, "Categories", text_clf.predict(X_All))
print(df_All)

df_All.to_csv("Dataframe1.csv")
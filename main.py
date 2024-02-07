import pandas as pd # Manipulate data
from IPython.display import display # To display the table

from sklearn.preprocessing import LabelEncoder # To transform the strings to int values
from sklearn.model_selection import train_test_split # To divide the data (into train and test)

from sklearn.ensemble import RandomForestClassifier # Decision Tree model 
from sklearn.neighbors import KNeighborsClassifier # Nearest Neighbors model

from sklearn.metrics import accuracy_score # To see the accuracy of the train


table = pd.read_csv("clients.csv")

# Checking that there aren't null values, but there are strings
#print(table.info())

encoder = LabelEncoder() # It will be used to transform the strings in numbers

# Transform all the columns that are strings to int (except the score_credito, that we are going to predict)
for coluna in table.columns:
    if table[coluna].dtype == "object" and coluna != "score_credito":
        table[coluna] = encoder.fit_transform(table[coluna])

# print(table.info()) 

predict = table["score_credito"] # Column that we are going to predict
calculate = table.drop(["score_credito", "id_cliente"], axis=1) # Columns that we are going to use to calculate

# Divide the data into train and test
calculate_train, calculate_test, predict_train, predict_test = train_test_split(calculate, predict, test_size=0.3, random_state=1)

# Assign the data into the two models
tree_model = RandomForestClassifier() # modelo arvore de decisao
neighbor_model = KNeighborsClassifier() # modelo do KNN (nearest neighbors - vizinhos mais proximos)

# Train the models
tree_model.fit(calculate_train, predict_train)
neighbor_model.fit(calculate_train, predict_train)

# Calculate the accuracy of the two models on test data
tree_accuracy_test = tree_model.score(calculate_test, predict_test)
neighbor_accuracy_test = neighbor_model.score(calculate_test, predict_test)

# Print the accuracy
#print("Random Forest Accuracy:", tree_accuracy_test) -> Accuracy: 82,46%
#print("KNN Accuracy:", neighbor_accuracy_test) -> Accuracy: 73,24%

# We are going to use the Tree model to predict new clients ("new_clients.csv")

# Making new predictions
new_clients = pd.read_csv("new_clients.csv")
display(new_clients)
for coluna in new_clients.columns:
    if new_clients[coluna].dtype == "object" and coluna != "score_credito":
        new_clients[coluna] = encoder.fit_transform(new_clients[coluna])

predictions = tree_model.predict(new_clients)
print(predictions)

# Trying to see the most important columns to the predictions calculos
columns = list(calculate_test.columns)
importance = pd.DataFrame(index=columns, data=tree_model.feature_importances_)
importance = importance * 100
print(importance)

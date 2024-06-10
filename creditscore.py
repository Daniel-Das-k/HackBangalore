# Load in our libraries
import pandas as pd
from sklearn.cluster import KMeans

dataset = pd.read_csv("/Users/danieldas/Downloads/train.csv")

x = dataset[["Annual_Income", "Num_of_Loan", "Monthly_Balance", "Changed_Credit_Limit"]]


range_n_clusters = [1,2,3]
scores = []

for i in range_n_clusters:
  kmeans = KMeans(n_clusters=i,max_iter = 1000,random_state=123)
  kmeans.fit(x)
  scores.append(kmeans.inertia_)

prediction = kmeans.predict(x.head(100))

print("Predicted Credit Score:", prediction)
####### This is the DEMO of the working of the Loaded model #########
import pandas as pd
import joblib

# Load the saved Random Forest model from the pickle file
loaded_model = joblib.load('/Users/danieldas/Downloads/credit_scoring.pkl')

# Assuming you have your input data stored in a DataFrame called 'input_data'
# Replace this with your actual input data
input_data = pd.DataFrame({
    "Annual_Income": [19114.12],
    "Num_of_Loan": [4.0],
    "Monthly_Balance": [312.494089],
    "Changed_Credit_Limit": [11.27] # Placeholder for prediction
})


# Preprocess the input data if necessary
# Make sure it matches the preprocessing done before training the model

# Predict using the loaded model
prediction = loaded_model.predict(input_data)

# Print the prediction
print("Prediction:", prediction)

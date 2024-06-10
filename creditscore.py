
import pandas as pd
from sklearn.cluster import KMeans
import pandas as pd
import joblib

dataset = pd.read_csv("train.csv")

x = dataset[["Annual_Income", "Num_of_Loan", "Monthly_Balance", "Changed_Credit_Limit"]]
range_n_clusters = [1,2,3]
scores = []

for i in range_n_clusters:
  kmeans = KMeans(n_clusters=i,max_iter = 1000,random_state=123)
  kmeans.fit(x)
  scores.append(kmeans.inertia_)

prediction = kmeans.predict(x.head(100))

print("Predicted Credit Score:", prediction)

loaded_model = joblib.load('credit_scoring.pkl')
input_data = pd.DataFrame({
    "Annual_Income": [19114.12],
    "Num_of_Loan": [4.0],
    "Monthly_Balance": [312.494089],
    "Changed_Credit_Limit": [11.27] 
})

prediction = loaded_model.predict(input_data)
print("Prediction:", prediction)

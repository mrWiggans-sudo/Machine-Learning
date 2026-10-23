# Import the required libraries
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Each customer: [monthly spending, monthly visits]
customer_data = [
    [1000,2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4]
]

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data)

# Create the KMeans model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train the model
cluster_labels = model.fit_predict(scaled_data)

# Display the groups
print("Customer Clustering Results")

for i, customer in enumerate(customer_data):
    print(
        f"Customer {i + 1}: "
        f"Spending = {customer[0]}, "
        f"Visits = {customer[1]}, "
        f"Cluster = {cluster_labels[i]}"
    )
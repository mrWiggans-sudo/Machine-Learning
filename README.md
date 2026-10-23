### Peter Kwame
# Machine Learning
Assignment on supervised and unsupervised machine learning 

# Supervised Machine Learning Project

Project Description:

This project introduces the fundamentals of supervised machine learning using Python. It demonstrates how to prepare a dataset, train a machine learning model, and make predictions using labelled data.

The project focuses on linear regression, a supervised learning algorithm that predicts continuous numerical values based on input features.

### Libraries Used

- Python

- Scikit-learn

- VS Code

### Initial Understanding

1. Understand the basics of supervised learning.

2. Prepare and organise a dataset.

3. Import and use LinearRegression from Scikit-learn.

4. Train a model using **`model.fit()`**.

5. Make predictions using **`model.predict()`**.

6. Understand how machine learning models learn patterns from data.

### How to Run the Project

1.  Install the required library:

        pip install scikit-learn

2.  Run the Python file:

        python supervised_ml.py

# Unsupervised Machine Learning Project

Project Description:

This project explores the fundamentals of unsupervised machine learning using Python. It demonstrates how to identify hidden patterns and group similar data points without using predefined labels.

The project focuses on K-Means Clustering, an unsupervised learning algorithm that groups data points into clusters based on their similarities.

### Libraries Used

- Python

- Scikit-learn

- VS Code

- StandardScaler
  
### Initial Process

1. Create a Python file named unsupervised_ml.py.

2. Import KMeans from **`sklearn.cluster`**.

3. Prepare customer data using a Python list.

4. Create a K-Means model with **`n_clusters=3`**.

5. Set **`random_state=42`** and **`n_init=10`**

6. Train the model on the customer dataset.

7. Display the cluster assigned to each customer.

8. Count the total number of customers in each cluster.

### How to Run the Project

1. Install the required library

        pip install scikit-learn

2. Run the Python file

        python unsupervised_ml.py
### Output 

- The program displays the cluster assigned to each customer and the total number of customers in each cluster.

- The exact cluster assignments and counts depend on the customer dataset.

### Install Dependencies

  Install Scikit-learn:

    python -m pip install --upgrade pip
    pip install scikit-learn

  Install the dependencies listed in requirements.txt:

    pip install -r requirements.txt

# Running the Project

**Supervised Machine Learning:** Linear Regression

Run the following command:

    python supervised_ml.py

Linear Regression learns the relationship between hours studied and exam scores, then predicts a score for a new number of study hours

Unsupervised Learning: K-Means Clustering

Run the following command:

    python unsupervised_ml.py

### Verify the Installation

 - Check installation:

        python -c "import sklearn; print(sklearn.__version__)"
# Theory Questions:
   
### What is supervised machine learning?
  - It is a labelled dataset, that carries both input and output perimeters.
### What is unsupervised machine learning?
  - Unsupervised Machine Learning is a type of machine learning where a computer learns patterns, structures, or relationships from data      without being provided with the correct answers in advance.
### Explain the difference between supervised and unsupervised learning.
- The key difference is that supervised learning uses labelled data to learn how to predict outcomes, while unsupervised learning uses unlabelled data to discover hidden patterns and relationships.
- **Supervised learning:** The model learns from examples with known answers to predict outcomes.
- **Unsupervised learning:** The model discovers patterns and groups in data without known target labels.
### Why is Linear Regression considered supervised learning?
- Linear Regression is considered Supervised Machine Learning because it learns from labelled data, where the correct data is already       known during training.
### Why is K-Means considered unsupervised learning?
- K-Means is considered Unsupervised Machine Learning because it discovers groups of similar data points without being given predefined     correct answers or labels.
- K-Means discovers groups by examining similarities in the data rather than learning from known customer categories.
### What is the difference between fit() and predict()?
- **`fit`**: Trains the model.
- **`predict`**: Uses the trained model to make predictions.
### Give two real-world applications of supervised learning and two of unsupervised learning.
  ### supervised learning:
 -  ***Weather forecasting:*** Weather data is labeled with the corresponding weather conditions
     (e.g., "sunny", "rainy", "snowy").
 - The model learns to predict future weather conditions based on current and historical data.
 - ***Credit card fraud detection:*** Models automatically identify and flag transactions that are likely to be fraudulent, helping             financial institutions and credit card companies prevent or minimise losses due to fraudulent activities.
   ### Unsupervised learning:
 - ***Anomaly detection:*** It can be understood using toy datasets to identify unusual patterns, outliers, or irregularities,                 enhancing algorithm understanding and performance evaluation.

# Dataset: hours studied and exam scores

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]

from sklearn.linear_model import LinearRegression

# prepare the data for training
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

# labels for the data
y = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# 4. Ask the user for hours studied
hours = float(input("Enter the number of hours studied: "))

# 5. Predict the exam score
prediction = model.predict([[hours]])

predicted_score = model.predict([[hours]])

print(f"Predicted exam score: {predicted_score[0]:.2f}")

# Save the prediction to a text file
with open("prediction.txt", "w") as file:
    file.write(f"Hours studied: {hours}\n")
    file.write(f"Predicted exam score: {predicted_score:.2f}\n")

print("Prediction saved to prediction.txt")
print(f"Predicted exam score: {predicted_score:.2f}")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Read in preprocessed data
df = pd.read_csv("gold_data_preprocessed.csv")

# Split data into training and testing sets
X = df.drop(["Time", "Gold_Price"], axis=1)
y = df["Gold_Price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict gold prices on test set
y_pred = lr_model.predict(X_test)

# Evaluate model performance
rmse = mean_squared_error(y_test, y_pred, squared=False)
print("Root Mean Squared Error:", rmse)

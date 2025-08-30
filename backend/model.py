import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import math

class PriceModel:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.model = LinearRegression()
        self.trained = False

    def train(self):
        X = self.df[["min_price", "max_price"]]
        y = self.df["modal_price"]
        self.model.fit(X, y)
        self.trained = True

    def predict(self, features):
        X_new = [[features["min_price"], features["max_price"]]]
        return float(self.model.predict(X_new)[0])

    def evaluate(self):
        # Predict for entire dataset
        X = self.df[["min_price", "max_price"]]
        y_true = self.df["modal_price"]
        y_pred = self.model.predict(X)
        
        r2 = r2_score(y_true, y_pred)  # R² Score
        mae = mean_absolute_error(y_true, y_pred)
        rmse = math.sqrt(mean_squared_error(y_true, y_pred))

        # Plot Actual vs Predicted
        plt.figure(figsize=(8,6))  # bigger figure
        plt.scatter(y_true, y_pred, color='green', alpha=0.6, s=50)
        plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', linewidth=2)
        plt.xlabel("Actual Modal Price", fontsize=14)
        plt.ylabel("Predicted Modal Price", fontsize=14)
        plt.title("Actual vs Predicted Modal Prices", fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()  # avoids cutting labels

        buf = BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode("utf-8")

        return {"r2": round(r2*100,2), "mae": round(mae,2), "rmse": round(rmse,2), "graph": img_base64}

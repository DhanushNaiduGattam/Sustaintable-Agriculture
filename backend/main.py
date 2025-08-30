from flask import Flask, request, jsonify, render_template
from model import PriceModel
import pandas as pd

CSV_PATH = r"G:\edunet\csv\final_dataset.csv"

app = Flask(__name__, template_folder="templates", static_folder="static")

price_model = PriceModel(CSV_PATH)
price_model.train()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        prediction = price_model.predict(data)
        return jsonify({"predicted_modal_price": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/data", methods=["GET"])
def get_data():
    df = pd.read_csv(CSV_PATH)
    df = df[["state","district","market","commodity","variety","min_price","max_price","modal_price"]]
    return jsonify(df.to_dict(orient="records"))

@app.route("/model_metrics", methods=["GET"])
def get_model_metrics():
    metrics = price_model.evaluate()
    return jsonify(metrics)

if __name__=="__main__":
    app.run(debug=True)

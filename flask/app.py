from flask import Flask, jsonify, request

import catboost as cb
import pandas as pd


model = cb.CatBoostClassifier()
model.load_model("model.cbm")

app = Flask("traffic_label")


# Setup prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get the provided JSON
    X = request.get_json()
    # Perform a prediction
    preds = model.predict(pd.DataFrame(X, index=[0]))[0][0]
    # Output json with prediction
    result = {"Label": preds}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host="0.0.0.0", port=8989)

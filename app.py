from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# !! Change ici le nom du fichier modèle :
model = pickle.load(open("logreg_model.pkl", "rb"))


def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])


@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Récupère les variables du formulaire
        credit_lines_outstanding = int(request.form["credit_lines_outstanding"])
        loan_amt_outstanding = float(request.form["loan_amt_outstanding"])
        total_debt_outstanding = float(request.form["total_debt_outstanding"])
        income = float(request.form["income"])
        years_employed = int(request.form["years_employed"])
        fico_score = int(request.form["fico_score"])

        features = {
            "credit_lines_outstanding": credit_lines_outstanding,
            "loan_amt_outstanding": loan_amt_outstanding,
            "total_debt_outstanding": total_debt_outstanding,
            "income": income,
            "years_employed": years_employed,
            "fico_score": fico_score,
        }

        # Prédiction avec le modèle
        prediction = model_pred(features)

        if prediction == 1:
            return render_template(
                "index.html",
                prediction_text="Attention : risque de défaut de crédit prédit.",
            )
        else:
            return render_template(
                "index.html", prediction_text="Pas de risque de défaut prédit."
            )
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

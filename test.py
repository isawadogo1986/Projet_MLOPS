from app import model_pred

# Nouveau dictionnaire avec les bonnes variables explicatives
new_data = {
    'credit_lines_outstanding': 4,
    'loan_amt_outstanding': 10000,
    'total_debt_outstanding': 20000,
    'income': 42000,
    'years_employed': 7,
    'fico_score': 680
}

def test_predict():
    prediction = model_pred(new_data)
    # Remplace '1' selon le résultat attendu pour ces caractéristiques
    assert prediction == 1, "incorrect prediction"

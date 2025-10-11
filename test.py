from app import model_pred

# Nouveau dictionnaire avec les bonnes variables explicatives
new_data = {
    'credit_lines_outstanding': 4,
    'loan_amt_outstanding': 3302.172238,
    'total_debt_outstanding': 813067.57021,
    'income': 50352.16821,
    'years_employed': 3,
    'fico_score': 545
}

def test_predict():
    prediction = model_pred(new_data)
    # Remplace '1' selon le résultat attendu pour ces caractéristiques
    assert prediction == 1, "incorrect prediction"

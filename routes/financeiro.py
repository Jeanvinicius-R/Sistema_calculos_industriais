from flask import Blueprint, render_template, request

financeiro_bp = Blueprint('financeiro', __name__)

@financeiro_bp.route('/financeiro', methods=['GET', 'POST'])
def financeiro():
    resultado = None
    alerta = None
    if request.method == 'POST':
        P = float(request.form['capital'])
        i = float(request.form['taxa']) / 100
        n = int(request.form['periodos'])

        M = P * (1 + i) ** n
        resultado = round(M, 2)

        if i > 0.08:
            alerta = "⚠️ Taxa acima do limite de 8% ao ano!"

    return render_template('financeiro.html', resultado=resultado, alerta=alerta)
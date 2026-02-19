from flask import Blueprint, render_template, request

temperatura_bp = Blueprint('temperatura', __name__)

@temperatura_bp.route('/temperatura', methods=['GET', 'POST'])
def temperatura():
    resultado = None
    if request.method == 'POST':
        valor     = float(request.form['valor'])
        conversao = request.form['conversao']

        if conversao == 'C_F':
            resultado = (9/5) * valor + 32
        elif conversao == 'C_K':
            resultado = valor + 273.15
        elif conversao == 'F_C':
            resultado = (5/9) * (valor - 32)
        elif conversao == 'K_C':
            resultado = valor - 273.15

        resultado = round(resultado, 2)

    return render_template('temperatura.html', resultado=resultado)
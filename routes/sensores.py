from flask import Blueprint, render_template, request

sensores_bp = Blueprint('sensores', __name__)

@sensores_bp.route('/sensores', methods=['GET', 'POST'])
def sensores():
    resultado = None
    if request.method == 'POST':
        decimal = int(request.form['valor'])
        if 0 <= decimal <= 255:
            binario = format(decimal, '08b')  # 8 bits com zeros à esquerda
            resultado = binario
        else:
            resultado = "Valor fora do range (0-255)"

    return render_template('sensores.html', resultado=resultado)
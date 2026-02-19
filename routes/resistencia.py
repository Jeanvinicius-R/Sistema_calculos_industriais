from flask import Blueprint, render_template, request

resistencia_bp = Blueprint('resistencia', __name__)

@resistencia_bp.route('/resistencia', methods=['GET', 'POST'])
def resistencia():
    resultado = None
    if request.method == 'POST':
        valores = request.form['resistencias'].split(',')
        tipo    = request.form['tipo']
        Rs      = [float(r) for r in valores]
        if tipo == 'serie':
            resultado = round(sum(Rs), 4)
        elif tipo == 'paralelo':
            resultado = round(1 / sum(1/r for r in Rs), 4)
    return render_template('resistencia.html', resultado=resultado)
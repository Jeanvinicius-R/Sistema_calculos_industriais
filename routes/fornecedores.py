from flask import Blueprint, render_template, request

fornecedores_bp = Blueprint('fornecedores', __name__)  # ← essa linha precisa existir

@fornecedores_bp.route('/fornecedores', methods=['GET', 'POST'])
def fornecedores():
    resultado = None
    if request.method == 'POST':
        preco     = float(request.form['preco'])
        qualidade = float(request.form['qualidade'])
        entrega   = float(request.form['entrega'])

        media = (preco * 0.4 + qualidade * 0.35 + entrega * 0.25) / (0.4 + 0.35 + 0.25)
        resultado = round(media, 2)

    return render_template('fornecedores.html', resultado=resultado)
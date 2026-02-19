from flask import Flask, render_template, request, jsonify  
from routes.fornecedores import fornecedores_bp
from routes.financeiro import financeiro_bp
from routes.sensores import sensores_bp
from routes.temperatura import temperatura_bp
from routes.resistencia import resistencia_bp

app = Flask(__name__)

app.register_blueprint(fornecedores_bp)
app.register_blueprint(financeiro_bp)
app.register_blueprint(sensores_bp)
app.register_blueprint(temperatura_bp)
app.register_blueprint(resistencia_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
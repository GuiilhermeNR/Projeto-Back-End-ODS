from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página do Projeto
@app.route('/projeto')
def projeto():
    return render_template('projeto.html')

# Rota para a página de Ideias
@app.route('/ideias')
def ideias():
    return render_template('ideias.html')

# Rota para a página do Autor
@app.route('/autor')
def autor():
    return render_template('autor.html')

# Rota para a página de Créditos
@app.route('/creditos')
def creditos():
    return render_template('creditos.html')

if __name__ == '__main__':
    app.run(debug=True)

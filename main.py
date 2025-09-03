from flask import Flask, request, render_template
import requests

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    if request.method == 'POST':
        termo = request.form['filtro']
        try:
            res = requests.post("http://localhost:5000/buscar", json={"termo": termo})
            if res.ok:
                resultados = res.json()
        except:
            resultados = ["⚠️ Cliente local não está ativo."]
    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)

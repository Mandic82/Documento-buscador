from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/buscar', methods=['POST'])
def buscar():
    termo = request.json.get('termo', '').lower()
    resultados = []
    caminhos = [os.path.expanduser("~/Documents"), os.path.expanduser("~/Desktop")]
    for caminho in caminhos:
        for root, dirs, files in os.walk(caminho):
            for file in files:
                if termo in file.lower():
                    resultados.append(os.path.join(root, file))
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(port=5000)

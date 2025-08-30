from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API da Sperb Tech funcionando!"

@app.route("/produtos")
def produtos():
    return jsonify([
        {"id": 1, "nome": "Lâmpada", "preco": 10.5, "estoque": 20},
        {"id": 2, "nome": "Tomada", "preco": 5.0, "estoque": 15}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

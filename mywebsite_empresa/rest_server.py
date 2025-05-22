from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/tienda2/venta', methods=['POST'])
def registrar_venta():
    data = request.get_json()
    producto = data.get('producto')
    cantidad = data.get('cantidad')
    print(f"[TIENDA 2] Venta registrada: Producto={producto}, Cantidad={cantidad}")
    return jsonify({"mensaje": "Venta registrada con éxito en TIENDA 2"})

if __name__ == '__main__':
    app.run(port=8002)

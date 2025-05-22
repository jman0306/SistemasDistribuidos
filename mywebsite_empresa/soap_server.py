from flask import Flask, request, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/soap', methods=['POST'])
def soap_server():
    xml_data = request.data.decode('utf-8')

    try:
        # Parsear el XML recibido
        root = ET.fromstring(xml_data)

        # Buscar los elementos dentro del Body
        producto = root.find('.//producto')
        cantidad = root.find('.//cantidad')

        print("[TIENDA 1] Venta registrada:")
        print(f"Producto: {producto.text if producto is not None else 'No encontrado'}")
        print(f"Cantidad: {cantidad.text if cantidad is not None else 'No encontrada'}")

    except ET.ParseError as e:
        print("Error al parsear XML:", e)

    # Respuesta SOAP simulada
    soap_response = """<?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
        <soapenv:Body>
            <response>Venta registrada con éxito en TIENDA 1 </response>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    return Response(soap_response, mimetype='text/xml')

if __name__ == '__main__':
    print("Servidor SOAP corriendo en http://localhost:8001/soap")
    app.run(port=8001)

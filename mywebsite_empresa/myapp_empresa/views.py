import requests
from django.http import HttpResponse
import xml.etree.ElementTree as ET

def recibe_ventas(request, sucursal, monto):
    producto = "Producto genérico"  # Puedes cambiar esto si deseas capturar más datos

    if sucursal == '1':
        soap_body = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
            <soapenv:Body>
                <venta>
                    <producto>{producto}</producto>
                    <cantidad>{monto}</cantidad>
                </venta>
            </soapenv:Body>
        </soapenv:Envelope>
        """
        headers = {'Content-Type': 'text/xml'}
        response = requests.post('http://localhost:8001/soap', data=soap_body.encode('utf-8'), headers=headers)
        tree = ET.fromstring(response.content)
        mensaje = tree.find('.//response')
        resultado = mensaje.text if mensaje is not None else "Respuesta SOAP no válida"

    elif sucursal == '2':
        response = requests.post('http://localhost:8002/tienda2/venta',
                                 json={'producto': producto, 'cantidad': monto})
        resultado = response.json().get('mensaje', 'Error en respuesta REST')

    else:
        resultado = "Sucursal no válida."

    return HttpResponse(resultado)

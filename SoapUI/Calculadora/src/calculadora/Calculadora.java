package calculadora;

import javax.xml.ws.Endpoint;

/**
 *
 * @author manri
 */

public class Calculadora {
    
    /* AL TERMINAR CORRER EN POWERSHELL
        Get-NetTCPConnection -LocalPort 8080 | Select-Object -ExpandProperty OwningProcess
        Stop-Process -Id (PID) -Force
    */
    public static void main(String[] args) {
        Endpoint.publish("http://localhost:8080/calculator", new ServicioCalculadora());
        System.out.println("Service published at http://localhost:8080/calculator?wsdl");
    }
    
}

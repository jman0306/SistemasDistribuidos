package consultapaises;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.List;

/**
 *
 * @author manri
 */

public class ConsultaPaises {

    /* AL TERMINAR CORRER EN POWERSHELL
        Get-NetTCPConnection -LocalPort 8080 | Select-Object -ExpandProperty OwningProcess
        Stop-Process -Id (PID) -Force
    */
    
    public static void main(String[] args) throws IOException {
        // Inicia el servidor HTTP en el puerto 8081
        HttpServer server = HttpServer.create(new InetSocketAddress(9090), 0);
        
        // Configura los endpoints
        server.createContext("/all", new AllCountriesHandler());
        server.createContext("/country", new CountryHandler());

        // Inicia el servidor
        server.start();
        System.out.println("Servidor iniciado en http://localhost:9090");
    }

    // Handler para la ruta /all que devuelve todos los países
    static class AllCountriesHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            List<Pais> countries = LectorPais.loadCountries("D:/manri/OneDrive ITAM/OneDrive - INSTITUTO TECNOLOGICO AUTONOMO DE MEXICO/Apuntes/Sistemas Distribuidos/Git/SistemasDistribuidos/SoapUI/countries.json");
            
            if (countries != null) {
                // Convierte la lista de países a JSON
                ObjectMapper mapper = new ObjectMapper();
                String response = mapper.writeValueAsString(countries);
                
                // Responde con los datos
                exchange.getResponseHeaders().set("Content-Type", "application/json");
                exchange.sendResponseHeaders(200, response.getBytes().length);
                
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
                os.close();
            } else {
                exchange.sendResponseHeaders(500, -1); // Error 500 si no se pudo cargar
            }
        }
    }

    // Handler para la ruta /country que busca un país específico
    static class CountryHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String query = exchange.getRequestURI().getQuery();
            String countryName = query != null ? query.split("=")[1] : null;
            
            List<Pais> countries = LectorPais.loadCountries("D:/manri/OneDrive ITAM/OneDrive - INSTITUTO TECNOLOGICO AUTONOMO DE MEXICO/Apuntes/Sistemas Distribuidos/Git/SistemasDistribuidos/SoapUI/countries.json");
            
            if (countryName != null && countries != null) {
                for (Pais country : countries) {
                    if (country.getName().equalsIgnoreCase(countryName)) {
                        // Convierte el país encontrado a JSON
                        ObjectMapper mapper = new ObjectMapper();
                        String response = mapper.writeValueAsString(country);
                        
                        exchange.getResponseHeaders().set("Content-Type", "application/json");
                        exchange.sendResponseHeaders(200, response.getBytes().length);
                        
                        OutputStream os = exchange.getResponseBody();
                        os.write(response.getBytes());
                        os.close();
                        return;
                    }
                }
                exchange.sendResponseHeaders(404, -1); // No se encontró el país
            } else {
                exchange.sendResponseHeaders(400, -1); // Bad request si no se pasa el nombre del país
            }
        }
    }
}

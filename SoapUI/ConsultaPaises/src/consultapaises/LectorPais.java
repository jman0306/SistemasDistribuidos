package consultapaises;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.util.List;

/**
 *
 * @author manri
 */
public class LectorPais {
    public static List<Pais> loadCountries(String path) {
        ObjectMapper mapper = new ObjectMapper();
        try {
            return mapper.readValue(new File(path), new TypeReference<List<Pais>>() {});
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }   
}

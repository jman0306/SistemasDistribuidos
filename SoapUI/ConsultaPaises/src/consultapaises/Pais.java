package consultapaises;

import java.util.List;

/**
 *
 * @author manri
 */
public class Pais {
    private String name;
    private List<String> topLevelDomain;
    private String alpha2Code;
    private String alpha3Code;
    private List<String> callingCodes;
    private String capital;
    private List<String> altSpellings;
    private String region;

    public Pais() {} // Constructor vacío para JSON

    public Pais(String name, List<String> topLevelDomain, String alpha2Code, String alpha3Code,
                   List<String> callingCodes, String capital, List<String> altSpellings, String region) {
        this.name = name;
        this.topLevelDomain = topLevelDomain;
        this.alpha2Code = alpha2Code;
        this.alpha3Code = alpha3Code;
        this.callingCodes = callingCodes;
        this.capital = capital;
        this.altSpellings = altSpellings;
        this.region = region;
    }

    // Getters y Setters

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public List<String> getTopLevelDomain() { return topLevelDomain; }
    public void setTopLevelDomain(List<String> topLevelDomain) { this.topLevelDomain = topLevelDomain; }

    public String getAlpha2Code() { return alpha2Code; }
    public void setAlpha2Code(String alpha2Code) { this.alpha2Code = alpha2Code; }

    public String getAlpha3Code() { return alpha3Code; }
    public void setAlpha3Code(String alpha3Code) { this.alpha3Code = alpha3Code; }

    public List<String> getCallingCodes() { return callingCodes; }
    public void setCallingCodes(List<String> callingCodes) { this.callingCodes = callingCodes; }

    public String getCapital() { return capital; }
    public void setCapital(String capital) { this.capital = capital; }

    public List<String> getAltSpellings() { return altSpellings; }
    public void setAltSpellings(List<String> altSpellings) { this.altSpellings = altSpellings; }

    public String getRegion() { return region; }
    public void setRegion(String region) { this.region = region; }
}

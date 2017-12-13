package es.joanmiralles;

public class RomanNumerals {

    public static final String ROMAN_I = "I";
    public static final String ROMAN_II = "II";
    public static final String ROMAN_III = "III";

    public String generate(int i) {
        if(i == 1) {
            return ROMAN_I;
        }else if (i == 2) {
            return ROMAN_II;
        }else {
            return ROMAN_III;
        }
    }
}

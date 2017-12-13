package es.joanmiralles;

public class RomanNumerals {

    public static final String ROMAN_I = "I";
    public static final String ROMAN_II = "II";

    public String generate(int i) {
        return i == 1 ? ROMAN_I : ROMAN_II;
    }
}

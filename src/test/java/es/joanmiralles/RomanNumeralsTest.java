package es.joanmiralles;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class RomanNumeralsTest {

    private RomanNumerals romanNumerals;

    @Test
    public void testRomanNumerals() {
        romanNumerals = new RomanNumerals();
        String result = romanNumerals.generate(1);
        assertThat(result, is("I"));
    }
}
package es.joanmiralles;

import org.junit.Before;
import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class RomanNumeralsTest {

    private RomanNumerals romanNumerals;

    @Before
    public void setUp() throws Exception {
        romanNumerals = new RomanNumerals();
    }

    @Test
    public void testRomanNumerals() {
        String result = romanNumerals.generate(1);
        assertThat(result, is("I"));
    }

    @Test
    public void testTwoReturnII(){
        String result = romanNumerals.generate(2);
        assertThat(result, is("II"));
    }

    @Test
    public void testThreeReturnIII(){
        String result = romanNumerals.generate(3);
        assertThat(result, is("III"));
    }


    @Test
    public void testFiveReturnV(){
        String result = romanNumerals.generate(5);
        assertThat(result, is("V"));
    }

    @Test
        public void testTenReturnX(){
            String result = romanNumerals.generate(10);
            assertThat(result, is("X"));
    }
    @Test
    public void testThirtyReturnXXX() {
        String result = romanNumerals.generate(30);
        assertThat(result, is("XXX"));
    }

    @Test
    public void testThirtySixReturnXXXVI() {
        String result = romanNumerals.generate(36);
        assertThat(result, is("XXXVI"));
    }
}
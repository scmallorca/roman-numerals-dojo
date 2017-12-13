package es.joanmiralles;

import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class RomanNumerals {

    public String generate(int i) {
        if (i < 5) {
            return RomanSymbol.I.times(i);
        } else {
            return RomanSymbol.V.name();
        }
    }

    enum RomanSymbol {
        I(1),
        V(5);

        private final int value;

        RomanSymbol(int value) {
            this.value = value;
        }

        String times(int i) {
            return IntStream.range(0, i).mapToObj(j -> this.name()).collect(Collectors.joining());
        }
    }
}

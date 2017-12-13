package es.joanmiralles;

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class RomanNumerals {

    public String generate(int i) {
        if (i >= 10) {
            return RomanSymbol.X.times(i);
        } else if (i >= 5) {
            return RomanSymbol.V.name();
        } else {
            return RomanSymbol.I.times(i);
        }
    }

    enum RomanSymbol {
        I(1, null),
        V(5, RomanSymbol.I),
        X(10, RomanSymbol.V);

        private final int value;
        private final RomanSymbol next;

        RomanSymbol(int value, RomanSymbol next) {
            this.value = value;
            this.next = next;
        }

        String times(int i) {
            return IntStream.range(0, i / this.value).
                    mapToObj(j -> this.name())
                    .collect(Collectors.joining());
        }
    }
}

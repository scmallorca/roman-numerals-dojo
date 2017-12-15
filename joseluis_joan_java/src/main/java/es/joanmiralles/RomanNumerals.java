package es.joanmiralles;

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class RomanNumerals {

    public String generate(int i) {
        return RomanSymbol.print(i);
    }

    enum RomanSymbol {
        I(1, null),
        V(5, RomanSymbol.I),
        X(10, RomanSymbol.V);

        private static final RomanSymbol MAX = X;
        private final int value;
        private final RomanSymbol next;

        RomanSymbol(int value, RomanSymbol next) {
            this.value = value;
            this.next = next;
        }

        static String print(int number) {
            String romanNumber = "";
            MAX.print(romanNumber,number);
            return romanNumber;
        }

        void print(String acc, int number) {
            acc += times(number / value);
            while(next != null) {
                next.print(acc,number % value);
            }
        }

        String times(int i) {
            return IntStream.range(0, i).
                    mapToObj(j -> this.name())
                    .collect(Collectors.joining());
        }
    }
}

package lambdasAndStreams;

import java.util.stream.IntStream;

public class SumOfNumber {
    public static void main(String[] args) {
        System.out.printf("The sum of 1 through 20 is : %d%n",
                IntStream.rangeClosed(1,20)
//                data source(  A stream pipeline begins with a method call that create the stream,known as the data source)
                        .sum());
    }
}

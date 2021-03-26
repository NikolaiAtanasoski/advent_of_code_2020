import java.util.List;
import java.util.stream.Collectors;

public class Day1 {

    public static void main(String[] args) {
        Day1 day1 = new Day1();
        day1.run();
    }

    public void run() {
        List<String> content = InputReader.readFileFromResourcesIntoList("day1_input.txt");
        List<Integer> numbers = content.stream().map(Integer::valueOf).collect(Collectors.toList());

        solvePuzzle1(numbers);
    }

    public void solvePuzzle1(List<Integer> numbers) {
        numbers.sort(Integer::compare);

        String answerToPuzzle1 = "";
        for (int i = 0; i < numbers.size(); i++) {

            int number1 = numbers.get(i);

            for (int j = i + 1; j < numbers.size(); j++) {

                int number2 = numbers.get(j);
                int result = number1 + number2;

                if (result == 2020) {
                    answerToPuzzle1 = "Answer is: " + number1 + " * " + number2 + (number1 * number2);
                    break;
                } else if (result > 2020) {
                    break;
                }
            }

            if (!answerToPuzzle1.isEmpty()) {
                break;
            }
        }

        System.out.println(answerToPuzzle1);
    }

}

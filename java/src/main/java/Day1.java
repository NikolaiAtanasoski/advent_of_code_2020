import java.util.List;

public class Day1 {

    public static void main(String[] args) {
        Day1 day1 = new Day1();
        day1.run();
    }

    public void run() {
        List<String> content = InputReader.readFileFromResourcesIntoList("testfile.txt");

        for(String line : content){
            System.out.println(line);
        }
    }

}

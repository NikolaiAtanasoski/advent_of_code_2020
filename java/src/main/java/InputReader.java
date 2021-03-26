import java.io.*;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class InputReader {


    public static List<String> readFileFromResourcesIntoList(String filename) {
        try {
            URL fileURL = InputReader.class.getClassLoader().getResource("input/" + filename);
            assert fileURL != null;
            File file = new File(fileURL.getFile());

            FileInputStream fileInputStream = new FileInputStream(file);
            InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream, StandardCharsets.ISO_8859_1);
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
            return bufferedReader.lines().collect(Collectors.toList());
        }
        catch (FileNotFoundException e) {
            System.out.println("NO file Found!");
            e.printStackTrace();
        }

        return Collections.emptyList();
    }

}

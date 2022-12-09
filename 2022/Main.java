import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello Day ");
        try {
            Scanner scanner = new Scanner(new File("input/-test.txt"));

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
            }
            scanner.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}

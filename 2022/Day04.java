import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day04 {
    public static void main(String[] args) {
        System.out.println("Hello Day 4");
        try {
            Scanner scanner = new Scanner(new File("input/04-input.txt"));
            int count = 0;
            int overlap = 0;
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] splited = line.split(",");
                String[] first = splited[0].split("-");
                int firstMin = Integer.parseInt(first[0]);
                int firstMax = Integer.parseInt(first[1]);

                String[] second = splited[1].split("-");
                int secondMin = Integer.parseInt(second[0]);
                int secondMax = Integer.parseInt(second[1]);
                
                // System.out.println("First: " + firstMin + " " + firstMax);
                // System.out.println("Second: " + secondMin + " " + secondMax);
                if ((firstMin <= secondMin && firstMax >= secondMax) || (firstMin >= secondMin && firstMax <= secondMax)) {
                    count++;
                }
                if ((firstMin <= secondMax && firstMin >= secondMin) || (secondMin <= firstMax && secondMin >= firstMin) ) {
                    overlap++;
                }

            }
            System.out.println("Superset count: " + count);
            System.out.println("Overlap count: " + overlap);
            scanner.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}

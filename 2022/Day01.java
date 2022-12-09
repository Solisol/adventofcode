import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Day01 {
    public static void main(String[] args) {
        System.out.println("Hello world");
        try {
            Scanner scanner = new Scanner(new File("input/01-input.txt"));
            ArrayList<Integer> elfs = new ArrayList<>();
            int elf = 0;
            int max = 0;
            elfs.add(elf, 0);
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                //System.out.println(line);
                if (line.equals("")) {
                    if (elfs.get(elf)> max) {
                        max = elfs.get(elf);
                    }
                    elf++;
                    elfs.add(elf, 0);
                } else {
                    elfs.add(elf, elfs.get(elf) + Integer.parseInt(line));
                }
                
            }
            System.out.println("Max calories: " + max);
            //System.out.println(elfs.toString());
            scanner.close();
            part2(elfs);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        
    }

    public static void part2(ArrayList<Integer> elfs) {
        Collections.sort(elfs, Collections.reverseOrder());
        int sumOfTop = elfs.get(0) + elfs.get(1) + elfs.get(2);
        System.out.println("Top three total calories: " + sumOfTop);

    }
}

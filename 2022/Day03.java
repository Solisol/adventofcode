import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;

public class Day03 {
    public static void main(String[] args) {
        System.out.println("Hello Day 3");
        //part1();
        part2();
    }

    public static void part2() {
        System.out.println("Hello Day 3 part 2");
        try {
            Scanner scanner = new Scanner(new File("input/03-input.txt"));
            int sum = 0;
            while (scanner.hasNextLine()) {
                String first = scanner.nextLine();
                String second = scanner.nextLine();
                String third = scanner.nextLine();

                char[] firsts = first.toCharArray();
                char[] seconds = second.toCharArray();
                char[] thirds = third.toCharArray();
                HashSet<Character> common = new HashSet<Character>();
                for (char f : firsts) {
                    for (char s : seconds) {
                        if (f == s) {
                            common.add(f);
                        }
                    }
                }
                for (char c : thirds) {
                    if (common.contains(c)) {
                        int value = (int) c;
                        if (Character.isUpperCase(c)) {
                            //System.out.println("True: " + c + " " + value);
                            sum += value - 38;
                        } else {
                            //System.out.println("False: " + c + " " + value);
                            sum += value - 96;
                        }
                        break;
                    }
                }
            }
            System.out.println("Sum Part 2: " + sum);
            scanner.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    public static void part1() {
        System.out.println("Hello Day 3 part 1");
        try {
            Scanner scanner = new Scanner(new File("input/03-input.txt"));
            int sum = 0;
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String first = line.substring(0, line.length()/2);
                String second = line.substring(line.length()/2);
                //System.out.println("First: " + first + " and Second: " + second);
                char[] firsts = first.toCharArray();
                char[] seconds = second.toCharArray();
                HashSet<Character> common = new HashSet<Character>();
                for (char f : firsts) {
                    for (char s : seconds) {
                        if (f == s) {
                            common.add(f);
                        }
                    }
                }
                for (Character c : common) {
                    int value = (int) c;
                    if (Character.isUpperCase(c)) {
                        //System.out.println("True: " + c + " " + value);
                        sum += value - 38;
                    } else {
                        //System.out.println("False: " + c + " " + value);
                        sum += value - 96;
                    }
                }
            }
            System.out.println("Sum Part 1: " + sum);
            scanner.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}

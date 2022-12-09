import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;

public class Day02 {
    public static void main(String[] args) {
        System.out.println("Day 2");
        int scorePart1 = 0;
        int scorePart2 = 0;
        try {
            Scanner scanner = new Scanner(new File("input/02-input.txt"));
            
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] round = line.split("\\s+");
                scorePart1 += part1(round);
                scorePart2 += part2(round);
                
            }
            System.out.println("Score part 1: " + scorePart1);
            System.out.println("Score part 2: " + scorePart2);
            
            scanner.close();
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static int part2(String[] round) {
        String you = round[1];
        String elf = round[0];
        int score = 0;
        if (you.equals("X")) {
            if (elf.equals("A")) {
                score += 3;
            } else if (elf.equals("B")) {
                score += 1;
            } else if (elf.equals("C")) {
                score += 2;
            }
        } else if (you.equals("Y")) {
            score += 3;
            if (elf.equals("A")) {
                score += 1;
            } else if (elf.equals("B")) {
                score += 2;
            } else if (elf.equals("C")) {
                score += 3;
            }
        } else if (you.equals("Z")) {
            score += 6;
            if (elf.equals("A")) {
                score += 2;
            } else if (elf.equals("B")) {
                score += 3;
            } else if (elf.equals("C")) {
                score += 1;
            }
        }
       return score;
    }

    public static int part1(String[] round) {
        String you = round[1];
        String elf = round[0];
        int score = 0;
        if (you.equals("X")) {
            score += 1;
            if (elf.equals("A")) {
                score += 3;
            } else if (elf.equals("C")) {
                score += 6;
            }
        } else if (you.equals("Y")) {
            score += 2;
            if (elf.equals("A")) {
                score += 6;
            } else if (elf.equals("B")) {
                score += 3;
            }
        } else if (you.equals("Z")) {
            score += 3;
            if (elf.equals("B")) {
                score += 6;
            } else if (elf.equals("C")) {
                score += 3;
            }
        }
       return score;
    }
    
}

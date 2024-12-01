package com.adventofcode;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Arrays;


public class Day01 {

    public static void main(String[] args) {
        try {
            List<String> input = Files.readAllLines(Path.of("input/day01.txt"));
            System.out.println("Part 1: " + solvePart1(input));
            System.out.println("Part 2: " + solvePart2(input));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static int solvePart1(List<String> input) {
        // Implement part 1 solution here
        int sum = 0;
        int[] left = new int[input.size()];
        int[] right = new int[input.size()];
        for (int a = 0; a < input.size(); a++) {
            String[] values = input.get(a).split("\\s+");
            left[a] = Integer.parseInt(values[0]);
            right[a] = Integer.parseInt(values[1]);
        }
        Arrays.sort(left);
        Arrays.sort(right);
        for (int i = 0; i < left.length; i++) {
            sum += Math.abs(left[i] - right[i]);
        }
        
        return sum;
    }

    static int solvePart2(List<String> input) {
        // Implement part 2 solution here
        int sum = 0;
        int[] left = new int[input.size()];
        int[] right = new int[input.size()];
        for (int a = 0; a < input.size(); a++) {
            String[] values = input.get(a).split("\\s+");
            left[a] = Integer.parseInt(values[0]);
            right[a] = Integer.parseInt(values[1]);
        }
        Arrays.sort(left);
        Arrays.sort(right);
        int last = -1;
        for (int i = 0; i < left.length; i++) {
            int occ = 0;
            if (left[i] != last) {
                for (int j = 0; j < left.length; j++) {
                    if (left[i] == right[j]) {
                        occ++;
                    } else if (right[j] > left[i]) {
                        break;
                    }
                }
            }
            sum += left[i] * occ;
        }
        
        return sum;
    }
}
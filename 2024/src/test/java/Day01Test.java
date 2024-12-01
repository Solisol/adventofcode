package com.adventofcode;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

class Day01Test {

    @Test
    void testSolvePart1() {
        List<String> input = List.of("3   4", "4   3", "2   5", "1   3", "3   9", "3   3");  // Replace with actual test data
        int expected = 11;  // Replace with the expected result for Part 1
        assertEquals(expected, Day01.solvePart1(input));
    }

    @Test
    void testSolvePart2() {
        List<String> input = List.of("3   4", "4   3", "2   5", "1   3", "3   9", "3   3");  // Replace with actual test data
        int expected = 31;  // Replace with the expected result for Part 2
        assertEquals(expected, Day01.solvePart2(input));
    }
}
package com.example.no_tests;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ExampleServiceTest {

    @Autowired
    private ExampleService exampleService;

    @Test
    void testGetGreeting() {
        String result = exampleService.getGreeting("John");
        assertEquals("Hello, John!", result);
    }

    @Test
    void testGetGreetingNullName() {
        String result = exampleService.getGreeting(null);
        assertEquals("Hello, Guest!", result);
    }

    @Test
    void testCalculateSum() {
        int result = exampleService.calculateSum(5, 10);
        assertEquals(15, result);
    }

    @Test
    void testCalculateSumNegativeNumbers() {
        int result = exampleService.calculateSum(-5, -10);
        assertEquals(-15, result);
    }
}

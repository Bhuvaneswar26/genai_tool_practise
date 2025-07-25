package com.example.no_tests;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
class ExampleControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void testGetGreetingEndpoint() throws Exception {
        mockMvc.perform(get("/api/greeting?name=John"))
                .andExpect(status().isOk())
                .andExpect(content().string("Hello, John!"));
    }

    @Test
    void testGetGreetingEndpointNoName() throws Exception {
        mockMvc.perform(get("/api/greeting"))
                .andExpect(status().isOk())
                .andExpect(content().string("Hello, Guest!"));
    }

    @Test
    void testCalculateSumEndpoint() throws Exception {
        mockMvc.perform(get("/api/sum?a=5&b=10"))
                .andExpect(status().isOk())
                .andExpect(content().string("15"));
    }
}

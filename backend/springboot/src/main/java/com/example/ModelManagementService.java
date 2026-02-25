package com.example;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ModelManagementService {

    @GetMapping("/models")
    public String listModels() {
        return "List of models";
    }
}
// Copyright (c) 2022 Nina Mathew All rights reserved
//
// Created by: Nina Mathew
// Created on: April 14, 2023
// This program does a for loop

#include <stdio.h>

void calculateArea() {
    float base;
    int ScanError = 0;
    float height;
    float area;
    // input
    printf("Enter the base of a triangle (cm): ");
    ScanError = scanf("%f", &base);
    printf("Enter the height of a triangle (cm): ");
    ScanError = scanf("%f", &height);

    if (ScanError == 0) {
        printf("Invalid input.\n");
    } else if (base < 0 || height < 0) {
        printf("Please Enter a Positive Number.\n");
    } else {
    // process
    area = base * height * 1/2;
    // output
    printf("The area is %.4f cm²\n\n", area);
}
}
int main() {
    // Call functions
    calculateArea();
    printf("\nDone.\n");
    return 0;
}

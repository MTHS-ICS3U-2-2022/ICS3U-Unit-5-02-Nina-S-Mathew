#!/usr/bin/env python3
""""
Created by: Nina Mathew
Created on: April 17, 2023
This is the " value of one number raised to the power of another. " module
"""


def calculate_area() -> None:
    """The calculate_area() function calculates area of a rectangle, returns None."""

    # process
    area = base * height * 1/2

    # output
    print(f"The area is {area:.4f} cm²")
    print("")

def main() -> None:
    """The main() function just calls other functions, returns None."""

    base_str = input("Enter the base of the triangle(cm): ")
    height_str = input("Enter the height of a triangle (cm): ")

    try:
        height_f = float(height_str)
        base_f = float(base_str)
        if height_f <= 0 or base_f <= 0:
    except ValueError:
        print("Please enter a positive number.")

        calculate_area(height_f, base_f)

    print("\nDone.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
""""
Created by: Nina Mathew
Created on: April 17, 2023
This is the " value of one number raised to the power of another. " module
"""


def calculate_area(base_f, height_f) -> None:
    """The calculate_area() function calculates area of a rectangle, returns None."""

    # process
    area = base_f * height_f * 1 / 2

    # output
    print(f"The area is {area:.4f} cm²")
    print("")


def main() -> None:
    """The main() function just calls other functions, returns None."""

    base_str = input("Enter the base of the triangle(cm): ")
    height_str = input("Enter the height of a triangle (cm): ")
    try:
        base_f = float(base_str)
        height_f = float(height_str)
        if base_f <= 0 or height_f <= 0:
            print("Please enter a positive number.")
        else:
            calculate_area(base_f, height_f)
    except ValueError:
        print("Invalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()

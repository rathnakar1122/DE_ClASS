def get_input():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length, width

def calculate_area(length, width):
    return length * width

def display_result(area):
    print(f"The area of the rectangle is: {area}")

def main():
    # Get user input
    length, width = get_input()
    # Calculate the area
    area = calculate_area(length, width)
    # Display the result
    display_result(area)

# This block of code ensures that the main function runs only when the program is run directly
if __name__ == "__main__":
    main()

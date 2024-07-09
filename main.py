import os
import json

# Get the list of available tests
test_list = [f.split(".")[0] for f in os.listdir("tests") if f.endswith(".json")]

# Display test list
def display_test_list():
    print("Available tests: ")
    for i, test in enumerate(test_list, start=1):
        test_info = get_test_info(test)
        print(f"{i}. {test_info['name']} - {test_info['description']}")

# Display information about each test
def get_test_info(test_name):
    with open(os.path.join("tests", f"{test_name}.json"), "r") as f:
        test_info = json.load(f)
    return test_info

def select_test():
    """
    Prompt the user to select a test from the available list.
    """
    display_test_list()
    while True:
        try:
            user_input = int(input("Enter the number of the test you want to run: "))
            if 1 <= user_input <= len(test_list):
                return test_list[user_input - 1]
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_test_details(test_info):
    """
    Display the details of the selected test.
    """
    print("\nTest Details:")
    print(f"Name: {test_info['name']}")
    print(f"Description: {test_info['description']}")
    print(f"Duration: {test_info['duration']}")
    print(f"Requirements: {test_info['requirements']}")
    print(f"Dimensions: {test_info['dimensions']}")
    print(f"Purpose: {test_info['purpose']}")



def main():
    """
    Main entry point for the tester UI.
    """
    print("Which test do you want to run?")

    # Allow the user to search or filter the list of available tests
    # (not implemented in this example)

    selected_test = select_test()
    test_info = get_test_info(selected_test)
    display_test_details(test_info)

    # Provide clear instructions
    # (not implemented in this example)

    # Implement the test execution and result handling
    # (not implemented in this example)

if __name__ == "__main__":
    main()
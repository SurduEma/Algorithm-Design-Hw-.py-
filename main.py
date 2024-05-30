import os
from element_division import divide_elements_among_workers
from data_generation import test_data_generation, random_test_data_generation

def main():
    input_file = "input_data.txt"

    if not os.path.exists(input_file):
        print("Error opening input file.")
        return

    with open(input_file, "r") as file:
        num_workers = int(file.readline().strip())
        num_elements = int(file.readline().strip())
        elements = [int(file.readline().strip()) for _ in range(num_elements)]

    divide_elements_among_workers(elements, num_elements, num_workers)

    # Uncomment these lines to generate data for testing
    # test_data_generation()
    # random_test_data_generation()

if __name__ == "__main__":
    main()

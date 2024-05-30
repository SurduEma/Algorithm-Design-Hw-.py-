import random
import time

def generate_and_save_elements(num_elements):
    elements = [100 * (i + 1) for i in range(num_elements)]
    with open("element_data.txt", "w") as file:
        for element in elements:
            file.write(f"{element}\n")

def generate_and_save_random_elements(num_elements):
    random.seed(time.time())
    elements = [random.randint(1, 100000000) for _ in range(num_elements)]
    with open("random_element_data.txt", "w") as file:
        for element in elements:
            file.write(f"{element}\n")

def test_data_generation():
    num_elements = int(input("Enter the number of elements for data generation: "))
    generate_and_save_elements(num_elements)
    print("Element data has been generated and saved to element_data.txt\n")

def random_test_data_generation():
    num_elements = int(input("Enter the number of elements for random data generation: "))
    generate_and_save_random_elements(num_elements)
    print("Random element data has been generated and saved to random_element_data.txt\n")

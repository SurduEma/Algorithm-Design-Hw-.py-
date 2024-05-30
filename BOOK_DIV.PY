import sys

def is_feasible(elements, n, k, mid):
    required_workers = 1
    current_load = 0

    for i in range(n):
        if elements[i] > mid:
            return False

        if current_load + elements[i] > mid:
            required_workers += 1
            current_load = elements[i]
            if required_workers > k:
                return False
        else:
            current_load += elements[i]

    return True

def find_optimal_load(elements, n, k):
    total_elements = sum(elements)
    left = 0
    right = total_elements
    result = sys.maxsize

    while left <= right:
        mid = (left + right) // 2
        if is_feasible(elements, n, k, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

def divide_elements_among_workers(elements, num_elements, num_workers):
    optimal_load = find_optimal_load(elements, num_elements, num_workers)
    output_file = "output_data.txt"

    try:
        with open(output_file, "w") as file:
            file.write("The optimal division of elements to minimize the maximum load is:\n")

            current_load = 0
            current_worker = 1
            start_idx = 0

            for i in range(num_elements):
                if current_load + elements[i] > optimal_load:
                    file.write(f"Worker {current_worker}: {current_load} units ( ")
                    for j in range(start_idx, i):
                        file.write(f"{elements[j]} ")
                    file.write(")\n")

                    current_load = elements[i]
                    current_worker += 1
                    start_idx = i
                else:
                    current_load += elements[i]

                if i == num_elements - 1:
                    file.write(f"Worker {current_worker}: {current_load} units ( ")
                    for j in range(start_idx, i + 1):
                        file.write(f"{elements[j]} ")
                    file.write(")\n")

            file.write(f"The optimal division of elements to minimize the maximum load is: {optimal_load} units\n")
    except IOError:
        print("Error opening output file.")

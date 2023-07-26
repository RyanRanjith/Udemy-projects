

## Used language is PYTHON##
import random

def sort_and_count_comparisons(arr):
    count = 0
    n = len(arr)

    for i in range(1, n):
        v = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > v:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1

        count += 1  # Increment count for the last comparison before the insertion
        arr[j + 1] = v

    return count


def main():
    sizes = [1000, 1500, 2000, 2500]

    for size in sizes:
        arr = generate_random_array(size)
        comparisons = sort_and_count_comparisons(arr)
        print(f"Array size: {size}, Comparisons: {comparisons}")


def generate_random_array(size):
    arr = [random.randint(-2147483648, 2147483647) for _ in range(size)]
    return arr


if __name__ == "__main__":
    main()

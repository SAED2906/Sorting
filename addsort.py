import time

def add_sort(tarr):
    # Dictionary to store counts within specific ranges
    sortedarr = {}

    # Variable to track the maximum range
    big = 0

    # Loop to count occurrences within ranges
    for x in tarr:
        # Calculate the offset to determine the range
        offset = x // 100
        # Create a unique key for each range
        c = 10 ** (x - offset * 100)

        # Update the maximum range
        if offset > big:
            big = offset

        try:
            # Update count within the range
            sortedarr[offset] += c
        except KeyError:
            # Initialize count if the range is encountered for the first time
            sortedarr[offset] = c

    # Reconstruct the sorted list
    sorted_list = []
    for offset in range(big + 1):
        try:
            # Retrieve the count and reconstruct the sorted list
            number = str(sortedarr[offset])
            count = len(number) - 1

            for j in number:
                for _ in range(int(j)):
                    sorted_list.append(count + offset * 100)

                count -= 1

        except KeyError:
            continue

    return sorted_list

# Example usage
tarr = [1, 2, 5, 10, 32, 11, 10, 9, 8, 20, 24, 21, 10, 345, 23, 87, 2123, 4675788, 15246, 9765,
        9, 8, 20, 24, 21, 10, 345, 23, 87, 2123, 4675788, 15246, 9765, 2, 632, 243, 11, 7958, 12357,
        58423, 346, 348, 2798, 2348, 2390, 434, 4455]

start_time = time.time()
result = add_sort(tarr)
end_time = time.time()

time_elapsed = end_time - start_time

print("Sorted List:", result)
print("Time Elapsed:", time_elapsed)

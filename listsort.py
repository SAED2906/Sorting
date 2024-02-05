import time

def list_sort(input_array):
    start_time = time.time()
    list_counts = {}                                                    # Dictionary to store counts for each element
    big = max(input_array, default=0)                                   # Find the maximum value in the array
    
    for x in input_array:                                               # Count occurrences of each element in the array
        try:
            list_counts[x] += 1                                         # If the element is already in the dictionary, update its count
        except KeyError:
            
            list_counts[x] = 1                                          # If the element is encountered for the first time, initialize its count
    
    end_time = time.time()
    time_elapsed = end_time - start_time
    
    result = []                                                         # Array output not included in time measure
    for x in range(big):                                                
        try:
            for _ in range(list_counts[x]):
                result.append(x)
        except:
            continue
    
    print("Sorted Array:", result)
    print("Time Elapsed for Counting:", time_elapsed)


input_array = [5, 3, 7, 2, 3, 5, 8, 4, 7, 1, 2, 6, 4, 8, 1, 6]
list_sort(input_array)

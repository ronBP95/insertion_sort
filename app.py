def insertion_sort(arr):
    operations = 0
    for i in range(len(arr)):
        num_we_are_on = arr[i]
        j = i - 1
        # do a check to see that we don't go out of range
        while j >= 0 and arr[j] > num_we_are_on:
                operations += 1
                # this check will be good, because we won't check arr[-1]
                # how can i scoot arr[j] up a place in our list
                arr[j+1] = arr[j]
                j -= 1
        # where am i
        j += 1
        arr[j] = num_we_are_on
    # ordered array
    return arr, operations

test_arr = [3, 4, 5, 8, 2, 1, 4]
ordered_array, operations = insertion_sort(test_arr)
print(ordered_array, operations)
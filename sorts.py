import math


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            array_comparision_swap(arr, i)
            swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end, start - 1, -1):
            array_comparision_swap(arr, i)
            swapped = True

        start += 1

    return arr

def array_comparision_swap(arr, i):
     if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
       
def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def counting_sort(arr):
    maximo = max(arr)
    count = [0] * (maximo + 1)
    for num in arr:
        count[num] += 1
    
    i = 0
    for val in range(0,maximo):
        while count[val] > 0:
            arr[i] = val
            i += 1
            count[val] -= 1
    return arr

def stalin_sort(arr):
    if len(arr) == 0:
        return arr
    
    kept = [arr[0]]
    max_so_far = arr[0] 

    for i in range(1, len(arr)):
        if arr[i] >= max_so_far:
            kept.append(arr[i])
            max_so_far = arr[i]
    return kept

def bogosort(arr):
    import random
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

def bucketSort(arr):
    
    max_value = max(arr)
    buckets = [[] for _ in range(max_value + 1)]

    for num in arr:
        bucketIndex = math.floor((num - 1)/3)
        buckets[bucketIndex].append(num)

    for bucket in buckets:
        bucket.sort()
    
    write_index = 0
    for bucket in buckets:
        for num in bucket:
            arr[write_index] = num
            write_index += 1
    return arr
            

if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample_array)
    sorted_array = merge_sort(sample_array)
    print("Sorted array (Merge Sort):", sorted_array)
    sorted_array = cocktail_sort(sample_array)
    print("Sorted array (Cocktail Sort):", sorted_array)
    sorted_array = heapSort(sample_array)
    print("Sorted array (Heap Sort):", sorted_array)
    sorted_array = counting_sort(sample_array)
    print("Sorted array (Counting Sort):", sorted_array)
    sorted_array = stalin_sort(sample_array)
    print("Sorted array (Stalin Sort):", sorted_array)
    sorted_array = bogosort(sample_array)
    print("Sorted array (Bogosort):", sorted_array)
    sorted_array = bucketSort(sample_array)
    print("Sorted array (Bucket Sort):", sorted_array)
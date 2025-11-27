[12, 45, 5, 67, 32, 66, 78, 10, 17, 9]

def quicksort_desc(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]     # lebih besar
    middle = [x for x in arr if x == pivot]  # sama
    right = [x for x in arr if x < pivot]    # lebih kecil
    return quicksort_desc(left) + middle + quicksort_desc(right)

data = [12, 45, 5, 67, 32, 66, 78, 10, 17, 9]

print("Data sebelum diurutkan:", data)
hasil = quicksort_desc(data)
print("Data setelah diurutkan (besar ke kecil):", hasil)

def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return 0.0000

    min_val, max_val = min(arr), max(arr)
    if max_val == min_val:
        return 0.0000

    buckets1 = [None] * n
    buckets2 = [None] * n
    bucket_sizes = [0] * n

    for num in arr:
        bucket_index = int((num - min_val) / ((max_val - min_val) / n))
        if bucket_index == n:
            bucket_index -= 1

        if bucket_sizes[bucket_index] == 0:
            buckets1[bucket_index] = num
            bucket_sizes[bucket_index] += 1
        elif bucket_sizes[bucket_index] == 1:
            buckets2[bucket_index] = num
            bucket_sizes[bucket_index] += 1
        elif bucket_index > 0:
            bucket_index -= 1
            if bucket_sizes[bucket_index] == 0:
                buckets1[bucket_index] = num
                bucket_sizes[bucket_index] += 1
            elif bucket_sizes[bucket_index] == 1:
                buckets2[bucket_index] = num
                bucket_sizes[bucket_index] += 1

    for i in range(n):
        if bucket_sizes[i] == 2 and buckets1[i] > buckets2[i]:
            buckets1[i], buckets2[i] = buckets2[i], buckets1[i]

    sorted_arr = []
    for i in range(n):
        if bucket_sizes[i] == 1:
            sorted_arr.append(buckets1[i])
        elif bucket_sizes[i] == 2:
            sorted_arr.extend([buckets1[i], buckets2[i]])

    max_gap = 0.0
    if sorted_arr:
        bucket_max = sorted_arr[0]
        for num in sorted_arr[1:]:
            max_gap = max(max_gap, num - bucket_max)
            bucket_max = num

    return round(max_gap, 4)


if __name__ == "__main__":
    n = int(input())
    coordinates = list(map(float, input().split()))
    max_gap = bucket_sort(coordinates)
    print(f"{max_gap:.4f}")


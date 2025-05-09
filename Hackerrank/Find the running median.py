import heapq

# Max heap for lower half (use negative values to simulate max heap)
max_heap = []
# Min heap for upper half
min_heap = []

def running_median(number, median):
    if len(min_heap) < len(max_heap):
        if number < median:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -number)
        else:
            heapq.heappush(min_heap, number)
        median = (min_heap[0] - max_heap[0]) / 2.0

    elif len(min_heap) > len(max_heap):
        if number > median:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, number)
        else:
            heapq.heappush(max_heap, -number)
        median = (min_heap[0] - max_heap[0]) / 2.0

    else:
        if number < median:
            heapq.heappush(max_heap, -number)
            median = -max_heap[0]
        else:
            heapq.heappush(min_heap, number)
            median = min_heap[0]

    return median

def main():
    n = int(input())
    median = 0.0

    for _ in range(n):
        number = int(input())
        median = running_median(number, median)
        print(f"{median:.1f}")

if __name__ == "__main__":
    main()

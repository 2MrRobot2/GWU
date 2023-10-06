import time
import heapq

def merge_sorted_lists(a,n):
    min_heap = [(size, [i]) for i, size in enumerate(a)]
    heapq.heapify(min_heap)
    
    total_cost = 0
    
    while len(min_heap) > 1:
        size1, list1 = heapq.heappop(min_heap)
        size2, list2 = heapq.heappop(min_heap)
        
        merged_list = list1 + list2
        merged_size = size1 + size2
        total_cost += merged_size
        
        # Limit the size of the merged list to `n`.
        if len(merged_list) > n:
            merged_list = merged_list[:n]
            merged_size = n
        
        heapq.heappush(min_heap, (merged_size, merged_list))
    
    merged_sequence = min_heap[0][1]
    
    return merged_sequence, total_cost

a = [3, 5, 2, 8]
n = 1000

merged_sequence, total_cost = merge_sorted_lists(a, n)

print("Merged sequence:", merged_sequence)
print("Total cost of merging:", total_cost)

start_time = time.time()
result = merge_sorted_lists(a, n)
end_time = time.time()
execution_time = end_time - start_time
execution_time_ns = execution_time * 1e9
print(f"Execution Time: {execution_time_ns:.6f} nanoseconds")

import heapq

def min_sort(cable_lengths):
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    while len(cable_lengths) > 1:
        min1 = heapq.heappop(cable_lengths)
        min2 = heapq.heappop(cable_lengths)
        current_cost = min1 + min2
        total_cost += current_cost
        
        heapq.heappush(cable_lengths, current_cost)
        
    return total_cost

cable_lengths = [8, 4, 6, 12, 16, 7]
min_cost = min_sort(cable_lengths)

print(min_cost)
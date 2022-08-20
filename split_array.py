
def isPossible(nums):
    
    freq_dist = Counter(nums)
    
    sequences = {}
    
    for num in nums:
        
        if freq_dist[num] == 0:
            continue
        
        # check if existing sequence can use 
        if num in sequences.keys() and sequences[num] > 0:
            
            sequences[num] = sequences[num] - 1
            
            if num + 1 in sequences.keys():
                sequences[num + 1] += 1
            else:
                sequences[num + 1] = 1
                
            freq_dist[num] = freq_dist[num] - 1
        # check if we can create a new sequence
        elif freq_dist[num] > 0 and freq_dist[num + 1] > 0 and freq_dist[num + 2] > 0:
            freq_dist[num] -= 1
            freq_dist[num + 1] -= 1
            freq_dist[num + 2] -= 1
            
            if num + 3 in sequences.keys():
                sequences[num + 3] += 1
            else:
                sequences[num + 3] = 1
        # list cannot be split
        else:
            return False
        
    return True
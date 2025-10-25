MOD = 10**9 + 7

def count_bitonic_upto(M):
    
    
    states = {}  # (n, v, phase) -> count
    
    
    # Initialize: single values (ascending phase)
    for k in range(1, M + 1):
        states[(k, k, 0)] = 1
    
    # Process each sum value
    for n in range(1, M + 1):
        # Extract current n states
        current_asc = {}  # v -> count (ascending)
        current_desc = {}  # v -> count (descending)
        
        for key in list(states.keys()):
            if key[0] == n:
                if key[2] == 0:  # ascending
                    current_asc[key[1]] = states[key]
                else:  # descending
                    current_desc[key[1]] = states[key]
        
        # Extend non-decreasing (ascending phase)
        for last, cnt in current_asc.items():
            for nxt in range(last, min(M + 1, M - n + last + 1)):
                new_n = n + nxt
                if new_n > M:
                    break
                key = (new_n, nxt, 0)
                states[key] = (states.get(key, 0) + cnt) % MOD
        
        # Start descent (transition from ascending to descending)
        for last, cnt in current_asc.items():
            for nxt in range(1, last):
                new_n = n + nxt
                if new_n > M:
                    break
                key = (new_n, nxt, 1)
                states[key] = (states.get(key, 0) + cnt) % MOD
        
        # Continue descent (descending phase)
        for last, cnt in current_desc.items():
            for nxt in range(1, min(last + 1, M - n + 2)):
                new_n = n + nxt
                if new_n > M:
                    break
                key = (new_n, nxt, 1)
                states[key] = (states.get(key, 0) + cnt) % MOD
        
        # Calculate result
        total = (sum(current_asc.values()) + sum(current_desc.values())) % MOD
        print(total, end=' ')
        
        # Delete old states
        for key in list(states.keys()):
            if key[0] == n:
                del states[key]

M = int(input().strip())
count_bitonic_upto(M)

def two_sum_indices(self, arr, target):
    mp = {}  # Dictionary to store element -> index
    for i, num in enumerate(arr):
        complement = target - num
        # If complement found, return indices
        if complement in mp:
            return [mp[complement], i]
        # Store current element and index
        mp[num] = i
    # No pair found
    return [-1, -1]

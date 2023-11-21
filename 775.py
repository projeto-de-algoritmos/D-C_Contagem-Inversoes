from typing import List

class Solution:
    def __init__(self):
        self.global_inversions = 0
        self.local_inversions = 0

    def combine(self, left, right):
        i, j = 0, 0
        temp = len(left)
        sorted_result = []

        while i < len(left) and j < len(right):
            if self.global_inversions > self.local_inversions:
                break;
            if left[i] <= right[j]:
                sorted_result.append(left[i])
                temp -= 1
                i += 1
            else:
                sorted_result.append(right[j])
                self.global_inversions += temp
                j += 1

        sorted_result += left[i:]
        sorted_result += right[j:]

        return sorted_result

    def count_global_inversions(self, arr):
        if len(arr) <= 1:
            return arr

        half_arr = len(arr) // 2

        left = self.count_global_inversions(arr[:half_arr])
        right = self.count_global_inversions(arr[half_arr:])

        combined_array = self.combine(left, right)

        return combined_array
    
    def count_local_inversions(self, arr):
        i = 0
        while i < len(arr):
            if i == len(arr)-1:
                break;
            
            if arr[i] > arr[i+1]:
                self.local_inversions += 1
            i += 1
  
    def isIdealPermutation(self, A: List[int]) -> bool:
        ci = Solution()
        ci.count_local_inversions(A)
        ci.count_global_inversions(A)
        
        if ci.global_inversions == ci.local_inversions:
            return True
        else:
            return False

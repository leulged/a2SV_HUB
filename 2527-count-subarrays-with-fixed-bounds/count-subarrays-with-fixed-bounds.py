from typing import List
from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_deque = deque()
        max_deque = deque()
        left = 0
        count = 0

        for right in range(len(nums)):

            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
                min_deque.clear()
                max_deque.clear()
                continue


            if nums[right] == minK:
                if min_deque:
                    min_deque.pop()
                min_deque.append(right)


            if nums[right] == maxK:
                if max_deque:
                    max_deque.pop()
                max_deque.append(right)


            if min_deque and max_deque:
                valid= min(min_deque[0], max_deque[0])  
                count += valid - left + 1 

        return count

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

            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()

            if nums[right] == minK:
                min_deque.append(right)

            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()

            if nums[right] == maxK:
                max_deque.append(right)


            if min_deque and max_deque:
                valid= min(min_deque[0], max_deque[0])  
                count += valid - left + 1 

        return count

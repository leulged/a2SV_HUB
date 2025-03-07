class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_sub = 1
        max_deque = deque()
        min_deque = deque()
        left = 0
        
        for i in range(len(nums)):
            while max_deque and nums[max_deque[-1]] <= nums[i]:
                max_deque.pop()
            max_deque.append(i)
            
            while min_deque and nums[min_deque[-1]] >= nums[i]:
                min_deque.pop()
            min_deque.append(i)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left = min(max_deque[0], min_deque[0]) + 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            max_sub = max(max_sub, i - left + 1)
        
        return max_sub

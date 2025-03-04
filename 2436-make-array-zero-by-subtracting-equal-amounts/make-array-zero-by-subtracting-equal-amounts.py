class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        len_set_num = len(set(nums))
        
        return len_set_num - 1 if 0 in nums else  len_set_num
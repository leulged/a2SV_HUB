class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        player1 = 0

        def score(left , right , nums):
            nonlocal player1
            if left == right:
                return nums[left]

            choice1 = nums[left] - score(left + 1 , right ,nums)
            choice2 = nums[right] - score(left  , right - 1 ,nums)

            player1 = max(choice1 , choice2)
            return player1
            
        temp = score(0 , len(nums) - 1, nums)

        return temp >= 0

        
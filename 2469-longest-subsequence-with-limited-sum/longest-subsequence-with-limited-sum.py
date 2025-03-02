class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        queries  = list(enumerate(queries))
        nums.sort()
        queries.sort(key = lambda  x : x[1])
        print(queries)
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        l = 1
        ans = [0] * len(queries)
        for i in range(len(queries)):
            while l < len(prefix):
                
                if prefix[l] <= queries[i][1]:
                    l += 1

                else:
                    break
            ans[queries[i][0]] = l - 1

        return ans



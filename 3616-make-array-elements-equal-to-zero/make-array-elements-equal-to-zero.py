class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ind = []
        for i in range(len(nums)):
            if nums[i] == 0:
                ind.append(i)
        count = 0
        for i in ind:
            left = nums[:]
            right = nums[:]
            #for left
            curr = i 
            
            flag = True
            while 0 <= curr < len(left):

                if left[curr] == 0:
                    if flag:
                        curr -= 1
                    else:
                        curr += 1

                else:
                    left[curr] -= 1
                    flag = not flag

                    if flag:
                        curr -= 1
                    else:
                        curr += 1
            if len(set(left)) == 1:
                count += 1
            
            #for right
            curr = i 
            
            flag = False
            while 0 <= curr < len(left):
                if right[curr] == 0:
                    if flag:
                        curr -= 1
                    else:
                        curr += 1

                else:
                    right[curr] -= 1
                    flag = not flag

                    if flag:
                        curr -= 1
                    else:
                        curr += 1
            if len(set(right)) == 1:
                count += 1
            print(left)
            print(right)
        return count

        
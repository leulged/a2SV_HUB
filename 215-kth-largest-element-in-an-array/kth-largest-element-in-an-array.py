class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify_down(heap, n, i):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right

            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                heapify_down(heap, n, smallest)

        n = len(nums)

        for i in range(n // 2 - 1 , -1 , -1):
            heapify_down(nums , n , i)
        
        for end in range(n - 1 , 0 , -1):
            nums[0] , nums[end] = nums[end] , nums[0]
            heapify_down(nums , end , 0)

        return nums[k - 1]

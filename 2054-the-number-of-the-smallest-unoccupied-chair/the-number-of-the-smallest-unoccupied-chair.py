class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = sorted([(arr, 1, i) for i, (arr, dep) in enumerate(times)] + 
                        [(dep, 0, i) for i, (arr, dep) in enumerate(times)])
        
        free_chairs = []
        occupied = {}  
        chair_pool = list(range(len(times)))  

        for time, is_arrival, friend in events:
            if not is_arrival:
                heappush(free_chairs, occupied[friend])
           
            else:

                if free_chairs:
                    chair = heappop(free_chairs)
                
                else:
                    chair = chair_pool.pop(0)
                
                occupied[friend] = chair
                if friend == targetFriend:
                    return chair

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = [False for _ in range(len(rooms))]
        queue = deque([0])
        
        while queue:
            node = queue.popleft()
            visit[node] = True
            for room in rooms[node]:
                if not visit[room]:
                    queue.append(room)
        
        for bol in visit:
            if not bol:
                return False
        
        return True